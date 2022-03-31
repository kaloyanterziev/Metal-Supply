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

from sawtooth_sdk.processor.exceptions import InvalidTransaction

from metal_supply_protobuf import payload_pb2


class MetalSupplyPayload(object):

    def __init__(self, payload):
        self._transaction = payload_pb2.MetalSupplyPayload()
        self._transaction.ParseFromString(payload)

    @property
    def action(self):
        return self._transaction.action

    @property
    def data(self):
        if self._transaction.HasField('create_agent') and \
            self._transaction.action == \
                payload_pb2.MetalSupplyPayload.CREATE_AGENT:
            return self._transaction.create_agent

        if self._transaction.HasField('create_record') and \
            self._transaction.action == \
                payload_pb2.MetalSupplyPayload.CREATE_RECORD:
            return self._transaction.create_record

        if self._transaction.HasField('transfer_record') and \
            self._transaction.action == \
                payload_pb2.MetalSupplyPayload.TRANSFER_RECORD:
            return self._transaction.transfer_record

        if self._transaction.HasField('link_record') and \
            self._transaction.action == \
                payload_pb2.MetalSupplyPayload.LINK_RECORD:
            return self._transaction.link_record

        if self._transaction.HasField('update_record_location') and \
            self._transaction.action == \
                payload_pb2.MetalSupplyPayload.UPDATE_RECORD_LOCATION:
            return self._transaction.update_record_location

        raise InvalidTransaction('Action does not match payload data')

    @property
    def timestamp(self):
        return self._transaction.timestamp
