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
