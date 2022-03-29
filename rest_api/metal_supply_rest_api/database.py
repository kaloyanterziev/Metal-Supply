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
# Modifications copyright (C) 2022 <Kaloyan Terizev>

import asyncio
import logging

import aiopg
import psycopg2
from psycopg2.extras import RealDictCursor


LATEST_BLOCK_NUM = """
SELECT max(block_num) FROM blocks
"""
LOGGER = logging.getLogger(__name__)


class Database(object):
    """Manages connection to the postgres database and makes async queries
    """
    def __init__(self, host, port, name, user, password, loop):
        self._dsn = 'dbname={} user={} password={} host={} port={}'.format(
            name, user, password, host, port)
        self._loop = loop
        self._pool = None

    async def connect(self, retries=5, initial_delay=1, backoff=2):
        """Initializes a connection to the database

        Args:
            retries (int): Number of times to retry the connection
            initial_delay (int): Number of seconds wait between reconnects
            backoff (int): Multiplies the delay after each retry
        """
        LOGGER.info('Connecting to database')

        delay = initial_delay
        for attempt in range(retries):
            try:
                self._pool = await aiopg.create_pool(
                    dsn=self._dsn, loop=self._loop, echo=True)
                LOGGER.info('Successfully connected to database')
                return

            except psycopg2.OperationalError:
                LOGGER.debug(
                    'Connection failed.'
                    ' Retrying connection (%s retries remaining)',
                    retries - attempt)
                await asyncio.sleep(delay)
                delay *= backoff

        self._pool = await aiopg.connect(
            dsn=self._dsn, loop=self._loop, echo=True)
        LOGGER.info('Successfully connected to database')

    def disconnect(self):
        """Closes connection to the database
        """
        self._pool.close()

    async def create_auth_entry(self,
                                public_key,
                                encrypted_private_key,
                                hashed_password):
        insert = """
        INSERT INTO auth (
            public_key,
            encrypted_private_key,
            hashed_password
        )
        VALUES ('{}', '{}', '{}');
        """.format(
            public_key,
            encrypted_private_key.hex(),
            hashed_password.hex())

        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                await cursor.execute(insert)

            conn.commit()

    async def create_agent_entry(self, public_key, name, email):
        insert = """
                INSERT INTO agents (
                    public_key,
                    name,
                    email
                )
                VALUES ('{}', '{}', '{}');
                """.format(
            public_key, name, email)
        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                await cursor.execute(insert)

            conn.commit()

    async def fetch_agent_resource(self, agent_id):
        fetch = """
        SELECT agents.id, agents.name, agents.email, agent_roles.name as role, agents.timestamp FROM agents
        JOIN agent_roles ON agents.role_id = agent_roles.id
        WHERE agents.id='{0}'
        AND ({1}) >= agents.start_block_num
        AND ({1}) < agents.end_block_num;
        """.format(agent_id, LATEST_BLOCK_NUM)

        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                await cursor.execute(fetch)
                return await cursor.fetchone()

    async def fetch_all_agent_resources(self):
        fetch = """
        SELECT agents.id, agents.name, agents.email, agent_roles.name as role, agents.timestamp FROM agents
        JOIN agent_roles ON agents.role_id = agent_roles.id
        WHERE ({0}) >= agents.start_block_num
        AND ({0}) < agents.end_block_num;
        """.format(LATEST_BLOCK_NUM)

        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                await cursor.execute(fetch)
                return await cursor.fetchall()

    async def fetch_agent_public_key(self, agent_id):
        fetch = """
            SELECT public_key 
            FROM agents
            WHERE id = {0};
        """.format(agent_id)
        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                await cursor.execute(fetch)
                return await cursor.fetchone()

    async def fetch_agent_on_email(self, email):
        fetch = """
        SELECT *
        FROM auth 
        JOIN agents ON auth.public_key = agents.public_key
        WHERE agents.email='{}'
        """.format(email)

        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                await cursor.execute(fetch)
                return await cursor.fetchone()

    async def fetch_auth_resource(self, public_key):
        fetch = """
        SELECT * FROM auth WHERE public_key='{}'
        """.format(public_key)

        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                await cursor.execute(fetch)
                return await cursor.fetchone()

    async def fetch_record_public_key(self, record_id):
        fetch = """
                   SELECT record_id 
                   FROM records
                   WHERE id = {0};
               """.format(record_id)
        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                await cursor.execute(fetch)
                return await cursor.fetchone()

    async def create_record_entry(self, record_public_key, material_type, material_origin, tonnes, contents, published):
        insert_records = """
            INSERT INTO records (
                record_id,
                material_type,
                material_origin,
                tonnes,
                published
            )
            VALUES ('{}', '{}', '{}', '{}', '{}');
        """.format(record_public_key, material_type, material_origin, tonnes, published)

        insert_record_contents = [
            """
            INSERT INTO record_contents (
            record_id,
            metal,
            percentage)
            VALUES ('{}', '{}', '{}');
            """.format(
                record_public_key,
                content['metal'],
                content['percentage'])
            for content in contents
        ]
        logging.debug(insert_records)
        logging.debug(insert_record_contents)
        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                await cursor.execute(insert_records)
                for insert in insert_record_contents:
                    await cursor.execute(insert)

            conn.commit()

    #TODO: delete
    async def fetch_record_resource(self, record_id):
        fetch_record = """
        SELECT record_id FROM records
        WHERE record_id='{0}'
        AND ({1}) >= start_block_num
        AND ({1}) < end_block_num;
        """.format(record_id, LATEST_BLOCK_NUM)

        fetch_record_locations = """
        SELECT latitude, longitude, timestamp FROM record_locations
        WHERE record_id='{0}'
        AND ({1}) >= start_block_num
        AND ({1}) < end_block_num;
        """.format(record_id, LATEST_BLOCK_NUM)

        fetch_record_owners = """
        SELECT id, percentage_owner FROM record_owners
        WHERE record_id='{0}'
        AND ({1}) >= start_block_num
        AND ({1}) < end_block_num;
        """.format(record_id, LATEST_BLOCK_NUM)

        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                try:
                    await cursor.execute(fetch_record)
                    record = await cursor.fetchone()

                    await cursor.execute(fetch_record_locations)
                    record['locations'] = await cursor.fetchall()

                    await cursor.execute(fetch_record_owners)
                    record['owners'] = await cursor.fetchall()

                    return record
                except TypeError as err:
                    LOGGER.error(err)
                    return None

    async def fetch_record_resource(self, record_public_key, agent_id, record_keys=None):
        if record_keys is None:
            record_keys = set()
        record_keys.add(record_public_key)
        fetch_record = """
        SELECT id, material_type, material_origin, tonnes, published FROM records
        WHERE record_id='{0}'
        AND ({1}) >= start_block_num
        AND ({1}) < end_block_num;
        """.format(record_public_key, LATEST_BLOCK_NUM)

        fetch_record_locations = """
        SELECT latitude, longitude, timestamp FROM record_locations
        WHERE record_id='{0}'
        AND agent_id='{1}'
        AND ({2}) >= start_block_num
        AND ({2}) < end_block_num;
        """.format(record_public_key, agent_id, LATEST_BLOCK_NUM)

        fetch_record_contents = """
                SELECT metal, percentage FROM record_contents
                WHERE record_id='{0}';
                """.format(record_public_key, LATEST_BLOCK_NUM)

        fetch_record_links = """
                        SELECT record_id FROM record_links
                        WHERE next_record_id='{0}';
                        """.format(record_public_key, LATEST_BLOCK_NUM)

        fetch_record_ownership = """
                SELECT percentage_owner FROM record_owners
                WHERE record_id='{0}'
                AND agent_id='{1}'
                AND ({2}) >= start_block_num
                AND ({2}) < end_block_num;
                """.format(record_public_key, agent_id, LATEST_BLOCK_NUM)

        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                try:
                    await cursor.execute(fetch_record)
                    record = await cursor.fetchone()

                    await cursor.execute(fetch_record_locations)
                    record['locations'] = await cursor.fetchall()

                    await cursor.execute(fetch_record_contents)
                    record['contents'] = await cursor.fetchall()

                    await cursor.execute(fetch_record_ownership)
                    record['tonnes'] = record['tonnes'] / 100.0 * (await cursor.fetchone())['percentage_owner']

                    await cursor.execute(fetch_record_links)
                    prev_record_ids = await cursor.fetchall()
                    prev_records = []
                    for prev_record_id_row in prev_record_ids:
                        prev_record_id = prev_record_id_row['record_id']
                        if prev_record_id not in record_keys:
                            prev_record = await self.fetch_record_resource(prev_record_id, agent_id, record_keys)
                            prev_records.append(prev_record)
                    record['prev_records'] = prev_records
                    return record
                except TypeError as err:
                    LOGGER.error(err)
                    return None

    async def fetch_all_record_resources(self):
        fetch_records = """
        SELECT id, record_id, material_type, material_origin, tonnes FROM records
        WHERE published 
        AND ({0}) >= start_block_num
        AND ({0}) < end_block_num;
        """.format(LATEST_BLOCK_NUM)

        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                try:
                    await cursor.execute(fetch_records)
                    records = await cursor.fetchall()

                    for record in records:
                        fetch_record_locations = """
                        SELECT latitude, longitude, timestamp
                        FROM record_locations
                        WHERE record_id='{0}'
                        AND published
                        AND ({1}) >= start_block_num
                        AND ({1}) < end_block_num;
                        """.format(record['record_id'], LATEST_BLOCK_NUM)

                        fetch_record_owners = """
                        SELECT agents.id, agents.name, record_owners.percentage_owner 
                        FROM record_owners
                        JOIN agents ON agents.public_key = record_owners.agent_id
                        WHERE record_owners.record_id='{0}'
                        AND ({1}) >= record_owners.start_block_num
                        AND ({1}) < record_owners.end_block_num;
                        """.format(record['record_id'], LATEST_BLOCK_NUM)

                        fetch_record_contents = """
                                        SELECT metal, percentage FROM record_contents
                                        WHERE record_id='{0}';
                                        """.format(record['record_id'], LATEST_BLOCK_NUM)

                        await cursor.execute(fetch_record_locations)
                        record['locations'] = await cursor.fetchall()

                        await cursor.execute(fetch_record_owners)
                        record['owners'] = await cursor.fetchall()

                        await cursor.execute(fetch_record_contents)
                        record['contents'] = await cursor.fetchall()

                        del record['record_id']

                    return records
                except TypeError as err:
                    LOGGER.error(err)
                    return []



    async def fetch_all_agent_records(self, agent_public_key):
        fetch_records = """
        SELECT records.id, records.record_id, records.material_type, records.material_origin, records.tonnes, records.published, record_owners.percentage_owner
        FROM records
        JOIN record_owners ON records.record_id = record_owners.record_id
        WHERE record_owners.agent_id = '{0}' 
        AND ({1}) >= records.start_block_num
        AND ({1}) < records.end_block_num;
        """.format(agent_public_key, LATEST_BLOCK_NUM)

        async with self._pool.acquire() as conn:
            async with conn.cursor(cursor_factory=RealDictCursor) as cursor:
                try:
                    await cursor.execute(fetch_records)
                    records = await cursor.fetchall()

                    for record in records:
                        fetch_record_locations = """
                        SELECT latitude, longitude, timestamp
                        FROM record_locations
                        WHERE record_id='{0}'
                        AND ({1}) >= start_block_num
                        AND ({1}) < end_block_num;
                        """.format(record['record_id'], LATEST_BLOCK_NUM)

                        fetch_record_contents = """
                        SELECT metal, percentage FROM record_contents
                        WHERE record_id='{0}';
                        """.format(record['record_id'], LATEST_BLOCK_NUM)

                        await cursor.execute(fetch_record_locations)
                        record['locations'] = await cursor.fetchall()

                        await cursor.execute(fetch_record_contents)
                        record['contents'] = await cursor.fetchall()

                        record['tonnes'] = record['tonnes'] / 100.0 * record['percentage_owner']

                        del record['record_id']
                        del record['percentage_owner']

                    return records
                except TypeError as err:
                    LOGGER.error(err)
                    return []
