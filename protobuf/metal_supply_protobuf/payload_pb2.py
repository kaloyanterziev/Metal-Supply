# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metal_supply_protobuf/payload.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metal_supply_protobuf import record_pb2 as metal__supply__protobuf_dot_record__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='metal_supply_protobuf/payload.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n#metal_supply_protobuf/payload.proto\x1a\"metal_supply_protobuf/record.proto\"\xe4\x02\n\x12MetalSupplyPayload\x12*\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x1a.MetalSupplyPayload.Action\x12(\n\x0c\x63reate_agent\x18\x02 \x01(\x0b\x32\x12.CreateAgentAction\x12*\n\rcreate_record\x18\x03 \x01(\x0b\x32\x13.CreateRecordAction\x12\x32\n\rupdate_record\x18\x04 \x01(\x0b\x32\x1b.UpdateRecordLocationAction\x12.\n\x0ftransfer_record\x18\x05 \x01(\x0b\x32\x15.TransferRecordAction\x12\x11\n\ttimestamp\x18\x06 \x01(\x04\"U\n\x06\x41\x63tion\x12\x10\n\x0c\x43REATE_AGENT\x10\x00\x12\x11\n\rCREATE_RECORD\x10\x01\x12\x11\n\rUPDATE_RECORD\x10\x02\x12\x13\n\x0fTRANSFER_RECORD\x10\x03\"/\n\x11\x43reateAgentAction\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\x05\"L\n\x12\x43reateRecordAction\x12\x11\n\trecord_id\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\"f\n\x1aUpdateRecordLocationAction\x12\x11\n\trecord_id\x18\x01 \x01(\t\x12\x10\n\x08latitude\x18\x02 \x01(\x12\x12\x11\n\tlongitude\x18\x03 \x01(\x12\x12\x10\n\x08\x61gent_id\x18\x04 \x01(\t\"V\n\x14TransferRecordAction\x12\x11\n\trecord_id\x18\x01 \x01(\t\x12\x17\n\x0freceiving_agent\x18\x02 \x01(\t\x12\x12\n\npercentage\x18\x03 \x01(\x01\x62\x06proto3'
  ,
  dependencies=[metal__supply__protobuf_dot_record__pb2.DESCRIPTOR,])



_METALSUPPLYPAYLOAD_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='MetalSupplyPayload.Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATE_AGENT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATE_RECORD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_RECORD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSFER_RECORD', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=347,
  serialized_end=432,
)
_sym_db.RegisterEnumDescriptor(_METALSUPPLYPAYLOAD_ACTION)


_METALSUPPLYPAYLOAD = _descriptor.Descriptor(
  name='MetalSupplyPayload',
  full_name='MetalSupplyPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='MetalSupplyPayload.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_agent', full_name='MetalSupplyPayload.create_agent', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_record', full_name='MetalSupplyPayload.create_record', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_record', full_name='MetalSupplyPayload.update_record', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer_record', full_name='MetalSupplyPayload.transfer_record', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='MetalSupplyPayload.timestamp', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METALSUPPLYPAYLOAD_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=432,
)


_CREATEAGENTACTION = _descriptor.Descriptor(
  name='CreateAgentAction',
  full_name='CreateAgentAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateAgentAction.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='CreateAgentAction.role', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=481,
)


_CREATERECORDACTION = _descriptor.Descriptor(
  name='CreateRecordAction',
  full_name='CreateRecordAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_id', full_name='CreateRecordAction.record_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='CreateRecordAction.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='CreateRecordAction.longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=483,
  serialized_end=559,
)


_UPDATERECORDLOCATIONACTION = _descriptor.Descriptor(
  name='UpdateRecordLocationAction',
  full_name='UpdateRecordLocationAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_id', full_name='UpdateRecordLocationAction.record_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='UpdateRecordLocationAction.latitude', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='UpdateRecordLocationAction.longitude', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='UpdateRecordLocationAction.agent_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=561,
  serialized_end=663,
)


_TRANSFERRECORDACTION = _descriptor.Descriptor(
  name='TransferRecordAction',
  full_name='TransferRecordAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_id', full_name='TransferRecordAction.record_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiving_agent', full_name='TransferRecordAction.receiving_agent', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percentage', full_name='TransferRecordAction.percentage', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=665,
  serialized_end=751,
)

_METALSUPPLYPAYLOAD.fields_by_name['action'].enum_type = _METALSUPPLYPAYLOAD_ACTION
_METALSUPPLYPAYLOAD.fields_by_name['create_agent'].message_type = _CREATEAGENTACTION
_METALSUPPLYPAYLOAD.fields_by_name['create_record'].message_type = _CREATERECORDACTION
_METALSUPPLYPAYLOAD.fields_by_name['update_record'].message_type = _UPDATERECORDLOCATIONACTION
_METALSUPPLYPAYLOAD.fields_by_name['transfer_record'].message_type = _TRANSFERRECORDACTION
_METALSUPPLYPAYLOAD_ACTION.containing_type = _METALSUPPLYPAYLOAD
DESCRIPTOR.message_types_by_name['MetalSupplyPayload'] = _METALSUPPLYPAYLOAD
DESCRIPTOR.message_types_by_name['CreateAgentAction'] = _CREATEAGENTACTION
DESCRIPTOR.message_types_by_name['CreateRecordAction'] = _CREATERECORDACTION
DESCRIPTOR.message_types_by_name['UpdateRecordLocationAction'] = _UPDATERECORDLOCATIONACTION
DESCRIPTOR.message_types_by_name['TransferRecordAction'] = _TRANSFERRECORDACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetalSupplyPayload = _reflection.GeneratedProtocolMessageType('MetalSupplyPayload', (_message.Message,), {
  'DESCRIPTOR' : _METALSUPPLYPAYLOAD,
  '__module__' : 'metal_supply_protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:MetalSupplyPayload)
  })
_sym_db.RegisterMessage(MetalSupplyPayload)

CreateAgentAction = _reflection.GeneratedProtocolMessageType('CreateAgentAction', (_message.Message,), {
  'DESCRIPTOR' : _CREATEAGENTACTION,
  '__module__' : 'metal_supply_protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:CreateAgentAction)
  })
_sym_db.RegisterMessage(CreateAgentAction)

CreateRecordAction = _reflection.GeneratedProtocolMessageType('CreateRecordAction', (_message.Message,), {
  'DESCRIPTOR' : _CREATERECORDACTION,
  '__module__' : 'metal_supply_protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:CreateRecordAction)
  })
_sym_db.RegisterMessage(CreateRecordAction)

UpdateRecordLocationAction = _reflection.GeneratedProtocolMessageType('UpdateRecordLocationAction', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERECORDLOCATIONACTION,
  '__module__' : 'metal_supply_protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:UpdateRecordLocationAction)
  })
_sym_db.RegisterMessage(UpdateRecordLocationAction)

TransferRecordAction = _reflection.GeneratedProtocolMessageType('TransferRecordAction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERRECORDACTION,
  '__module__' : 'metal_supply_protobuf.payload_pb2'
  # @@protoc_insertion_point(class_scope:TransferRecordAction)
  })
_sym_db.RegisterMessage(TransferRecordAction)


# @@protoc_insertion_point(module_scope)
