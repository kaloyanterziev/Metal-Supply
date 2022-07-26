# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------
# Modifications copyright (C) 2022 <Kaloyan Terziev>

import datetime
from json.decoder import JSONDecodeError
import logging
import time

from aiohttp.web import json_response
import bcrypt
from Crypto.Cipher import AES
from itsdangerous import BadSignature
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from metal_supply_rest_api.errors import ApiBadRequest
from metal_supply_rest_api.errors import ApiNotFound
from metal_supply_rest_api.errors import ApiUnauthorized


LOGGER = logging.getLogger(__name__)


class RouteHandler(object):
    def __init__(self, loop, messenger, database):
        self._loop = loop
        self._messenger = messenger
        self._database = database

    async def authenticate(self, request):
        body = await decode_request(request)
        required_fields = ['email', 'password']
        validate_fields(required_fields, body)

        password = bytes(body.get('password'), 'utf-8')

        auth_info = await self._database.fetch_agent_on_email(
            body.get('email'))
        if auth_info is None:
            raise ApiUnauthorized('No agent with that email exists')

        hashed_password = auth_info.get('hashed_password')
        if not bcrypt.checkpw(password, bytes.fromhex(hashed_password)):
            raise ApiUnauthorized('Incorrect email or password')

        token = generate_auth_token(
            request.app['secret_key'], auth_info.get('public_key'))
        return json_response({
            'id': auth_info.get('id'),
            'authorization': token,
            'name': auth_info.get('name'),
            'email': auth_info.get('email'),
            'role': auth_info.get('role_id'),
            'company': auth_info.get('company')
        })

    async def create_agent(self, request):
        body = await decode_request(request)
        required_fields = ['name', 'email', 'password', 'role', 'company']
        validate_fields(required_fields, body)

        public_key, private_key = self._messenger.get_new_key_pair()

        id_of_row = await self._database.create_agent_entry(public_key, body.get('name'), body.get('email'), body.get('company'))

        await self._messenger.send_create_agent_transaction(
            private_key=private_key,
            role=body.get('role'),
            timestamp=get_time())

        encrypted_private_key = encrypt_private_key(
            request.app['aes_key'], public_key, private_key)
        hashed_password = hash_password(body.get('password'))

        await self._database.create_auth_entry(
            public_key, encrypted_private_key, hashed_password)

        token = generate_auth_token(
            request.app['secret_key'], public_key)

        return json_response({
            'authorization': token,
            'id': id_of_row,
            'public_key': public_key,
            'private_key': private_key
        })

    async def list_agents(self, _request):
        agent_list = await self._database.fetch_all_agent_resources()
        return json_response(agent_list)

    async def fetch_agent(self, request):
        agent_id = request.match_info.get('agent_id', '')
        agent = await self._database.fetch_agent_resource(agent_id)
        if agent is None:
            raise ApiNotFound(
                'Agent with public key {} was not found'.format(agent_id))
        return json_response(agent)

    async def fetch_agent_records(self, request):
        _, agent_public_key = await self._authorize(request)
        records = await self._database.fetch_all_agent_records(agent_public_key)
        # if records is None:
        #     raise ApiNotFound(
        #         'Agent with public key {} was not found'.format(agent_public_key))
        return json_response(records)

    async def create_record(self, request):
        private_key, _ = await self._authorize(request)
        record_public_key, _ = self._messenger.get_new_key_pair()

        body = await decode_request(request)
        required_fields = ['latitude', 'longitude', 'material_type', 'material_origin', 'contents', 'tonnes']
        validate_fields(required_fields, body)

        await self._database.create_record_entry(record_public_key, body.get('public', False))

        await self._messenger.send_create_record_transaction(
            private_key=private_key,
            record_id=record_public_key,
            latitude=body.get('latitude'),
            longitude=body.get('longitude'),
            material_type=body.get('material_type'),
            material_origin=body.get('material_origin'),
            contents=body.get('contents'),
            tonnes=body.get('tonnes'),
            timestamp=get_time())

        return json_response(
            {'data': 'Create record transaction submitted'})

    async def list_records(self, _request):
        record_list = await self._database.fetch_all_record_resources()
        return json_response(record_list)

    async def fetch_record(self, request):
        record_id = request.match_info.get('record_id', '')
        record_public_key = (await self._database.fetch_record_public_key(record_id))['record_id']
        _, agent_public_key = await self._authorize(request)
        record = await self._database.fetch_record_resource(record_public_key, agent_public_key)
        if record is None:
            raise ApiNotFound(
                'Record with the record id '
                '{} was not found'.format(record_id))
        return json_response(record)

    async def transfer_record(self, request):
        private_key, _ = await self._authorize(request)

        body = await decode_request(request)
        required_fields = ['receiving_agent', 'percentage']
        validate_fields(required_fields, body)

        record_id = request.match_info.get('record_id', '')
        record_public_key = (await self._database.fetch_record_public_key(record_id))['record_id']
        receiving_agent = await self._database.fetch_agent_public_key(body['receiving_agent'])

        await self._messenger.send_transfer_record_transaction(
            private_key=private_key,
            receiving_agent=receiving_agent['public_key'],
            percentage=body['percentage'],
            record_id=record_public_key,
            timestamp=get_time())

        return json_response(
            {'data': 'Transfer record transaction submitted'})

    async def link_record(self, request):
        private_key, _ = await self._authorize(request)

        record_id = request.match_info.get('record_id', '')
        next_record_id = request.match_info.get('next_record_id', '')
        record_public_key = (await self._database.fetch_record_public_key(record_id))['record_id']
        next_record_public_key = (await self._database.fetch_record_public_key(next_record_id))['record_id']

        await self._messenger.send_link_record_transaction(
            private_key=private_key,
            record_id = record_public_key,
            next_record_id = next_record_public_key,
            timestamp=get_time())

        return json_response(
            {'data': 'Linking record transaction submitted'})

    async def update_record_location(self, request):
        private_key, public_key = await self._authorize(request)

        body = await decode_request(request)
        required_fields = ['latitude', 'longitude']
        validate_fields(required_fields, body)

        record_id = request.match_info.get('record_id', '')
        record_public_key = (await self._database.fetch_record_public_key(record_id))['record_id']

        await self._messenger.send_update_record_location_transaction(
            private_key=private_key,
            public_key=public_key,
            latitude=body['latitude'],
            longitude=body['longitude'],
            record_id=record_public_key,
            timestamp=get_time())

        return json_response(
            {'data': 'Update record transaction submitted'})

    # TODO: finish the update
    async def update_record(self, request):
        private_key, _ = await self._authorize(request)

        body = await decode_request(request)
        required_fields = ['latitude', 'longitude']
        validate_fields(required_fields, body)

        record_id = request.match_info.get('record_id', '')
        record_public_key = (await self._database.fetch_record_public_key(record_id))['record_id']

        await self._messenger.send_update_record_location_transaction(
            private_key=private_key,
            latitude=body['latitude'],
            longitude=body['longitude'],
            record_id=record_public_key,
            timestamp=get_time())

        return json_response(
            {'data': 'Update record transaction submitted'})

    async def _authorize(self, request):
        token = request.headers.get('AUTHORIZATION')
        if token is None:
            raise ApiUnauthorized('No auth token provided')
        token_prefixes = ('Bearer', 'Token')
        for prefix in token_prefixes:
            if prefix in token:
                token = token.partition(prefix)[2].strip()
        try:
            token_dict = deserialize_auth_token(request.app['secret_key'],
                                                token)
        except BadSignature:
            raise ApiUnauthorized('Invalid auth token')
        public_key = token_dict.get('public_key')
        auth_resource = await self._database.fetch_auth_resource(public_key)
        if auth_resource is None:
            raise ApiUnauthorized('Token is not associated with an agent')
        private_key = decrypt_private_key(request.app['aes_key'],
                                   public_key,
                                   auth_resource['encrypted_private_key'])
        return private_key, public_key


async def decode_request(request):
    try:
        return await request.json()
    except JSONDecodeError:
        raise ApiBadRequest('Improper JSON format')


def validate_fields(required_fields, body):
    for field in required_fields:
        if body.get(field) is None:
            raise ApiBadRequest(
                "'{}' parameter is required".format(field))


def encrypt_private_key(aes_key, public_key, private_key):
    init_vector = bytes.fromhex(public_key[:32])
    cipher = AES.new(bytes.fromhex(aes_key), AES.MODE_CBC, init_vector)
    return cipher.encrypt(private_key)


def decrypt_private_key(aes_key, public_key, encrypted_private_key):
    init_vector = bytes.fromhex(public_key[:32])
    cipher = AES.new(bytes.fromhex(aes_key), AES.MODE_CBC, init_vector)
    private_key = cipher.decrypt(bytes.fromhex(encrypted_private_key))
    return private_key


def hash_password(password):
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


def get_time():
    dts = datetime.datetime.utcnow()
    return round(time.mktime(dts.timetuple()) + dts.microsecond/1e6)


def generate_auth_token(secret_key, public_key):
    serializer = Serializer(secret_key)
    token = serializer.dumps({'public_key': public_key})
    return token.decode('ascii')


def deserialize_auth_token(secret_key, token):
    serializer = Serializer(secret_key)
    return serializer.loads(token)
