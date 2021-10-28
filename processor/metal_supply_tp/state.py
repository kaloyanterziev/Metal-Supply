from metal_supply_addressing import addresser

from metal_supply_protobuf import agent_pb2
from metal_supply_protobuf import record_pb2


class MetalSupplyState(object):
    def __init__(self, context, timeout=2):
        self._context = context
        self._timeout = timeout

    def get_agent(self, public_key) -> agent_pb2.Agent:
        """Gets the agent associated with the public_key

        Args:
            public_key (str): The public key of the agent

        Returns:
            agent_pb2.Agent: Agent with the provided public_key
        """
        address = addresser.get_agent_address(public_key)
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            container = agent_pb2.AgentContainer()
            container.ParseFromString(state_entries[0].data)
            for agent in container.entries:
                if agent.public_key == public_key:
                    return agent

        return None

    def set_agent(self, public_key, name, role, timestamp):
        """Creates a new agent in state

        Args:
            public_key (str): The public key of the agent
            name (str): The human-readable name of the agent
            role (enum): The role of the Agent
            timestamp (int): Unix UTC timestamp of when the agent was created
        """
        address = addresser.get_agent_address(public_key)
        agent = agent_pb2.Agent(
            public_key=public_key, name=name, role=role, timestamp=timestamp)
        container = agent_pb2.AgentContainer()
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            container.ParseFromString(state_entries[0].data)

        container.entries.extend([agent])
        data = container.SerializeToString()

        updated_state = {}
        updated_state[address] = data
        self._context.set_state(updated_state, timeout=self._timeout)

    def get_record(self, record_id) -> record_pb2.Record:
        """Gets the record associated with the record_id

        Args:
            record_id (str): The id of the record

        Returns:
            record_pb2.Record: Record with the provided record_id
        """
        address = addresser.get_record_address(record_id)
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            container = record_pb2.RecordContainer()
            container.ParseFromString(state_entries[0].data)
            for record in container.entries:
                if record.record_id == record_id:
                    return record

        return None

    def set_record(self,
                   public_key,
                   latitude,
                   longitude,
                   record_id,
                   material_type,
                   material_origin,
                   contents,
                   timestamp):
        """Creates a new record in state

        Args:
            public_key (str): The public key of the agent creating the record
            latitude (int): Initial latitude of the record
            longitude (int): Initial latitude of the record
            record_id (str): Unique ID of the record
            timestamp (int): Unix UTC timestamp of when the agent was created
        """
        address = addresser.get_record_address(record_id)

        contents = [record_pb2.Record.Content(percentage=content.percentage, metal=content.metal) for content in contents]
        owner = record_pb2.Record.Owner(
            agent_id=public_key,
            timestamp=timestamp,
            percentage=100.0)
        location = record_pb2.Record.Location(
            latitude=latitude,
            longitude=longitude,
            agent_id=public_key,
            timestamp=timestamp)
        record = record_pb2.Record(
            record_id=record_id,
            owners=[owner],
            locations=[location],
            material_type=material_type,
            material_origin=material_origin,
            contents=contents)
        container = record_pb2.RecordContainer()
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            container.ParseFromString(state_entries[0].data)

        container.entries.extend([record])
        data = container.SerializeToString()

        updated_state = {}
        updated_state[address] = data
        self._context.set_state(updated_state, timeout=self._timeout)

    def transfer_record(self, receiving_agent, sending_agent, record_id, timestamp, percentage):

        address = addresser.get_record_address(record_id)
        container = record_pb2.RecordContainer()
        record = record_pb2.Record()
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            container.ParseFromString(state_entries[0].data)
            for record_entry in container.entries:
                if record_entry.record_id == record_id:
                    record = record_entry

        sending_owner = next(owner for owner in record.owners if owner.agent_id == sending_agent)
        receiving_owner = next((owner for owner in record.owners if owner.agent_id == receiving_agent), None)
        receiving_percentage = percentage * sending_owner.percentage / 100.0
        sending_owner.percentage -= receiving_percentage

        if receiving_owner is None :
            owner = record_pb2.Record.Owner(
                agent_id=receiving_agent,
                timestamp=timestamp,
                percentage=receiving_percentage)
            record.owners.extend([owner])
        else:
            receiving_owner.percentage += receiving_percentage


        data = container.SerializeToString()
        updated_state = {}
        updated_state[address] = data
        self._context.set_state(updated_state, timeout=self._timeout)

    def update_record_location(self, latitude, longitude, record_id, agent_id, timestamp):
        location = record_pb2.Record.Location(
            latitude=latitude,
            longitude=longitude,
            agent_id=agent_id,
            timestamp=timestamp)
        address = addresser.get_record_address(record_id)
        container = record_pb2.RecordContainer()
        state_entries = self._context.get_state(
            addresses=[address], timeout=self._timeout)
        if state_entries:
            container.ParseFromString(state_entries[0].data)
            for record in container.entries:
                if record.record_id == record_id:
                    record.locations.extend([location])
        data = container.SerializeToString()
        updated_state = {}
        updated_state[address] = data
        self._context.set_state(updated_state, timeout=self._timeout)
