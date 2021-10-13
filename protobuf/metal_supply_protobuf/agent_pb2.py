# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='agent.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x61gent.proto\"\x8d\x01\n\x05\x41gent\x12\x12\n\npublic_key\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x04role\x18\x03 \x01(\x0e\x32\x0b.Agent.Role\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\"4\n\x04Role\x12\x0c\n\x08RECYCLER\x10\x00\x12\r\n\tCONVERTER\x10\x01\x12\x0f\n\x0bWASTE_OWNER\x10\x02\")\n\x0e\x41gentContainer\x12\x17\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x06.Agentb\x06proto3'
)



_AGENT_ROLE = _descriptor.EnumDescriptor(
  name='Role',
  full_name='Agent.Role',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RECYCLER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONVERTER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WASTE_OWNER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=105,
  serialized_end=157,
)
_sym_db.RegisterEnumDescriptor(_AGENT_ROLE)


_AGENT = _descriptor.Descriptor(
  name='Agent',
  full_name='Agent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='Agent.public_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='Agent.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role', full_name='Agent.role', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Agent.timestamp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AGENT_ROLE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=157,
)


_AGENTCONTAINER = _descriptor.Descriptor(
  name='AgentContainer',
  full_name='AgentContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='AgentContainer.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=159,
  serialized_end=200,
)

_AGENT.fields_by_name['role'].enum_type = _AGENT_ROLE
_AGENT_ROLE.containing_type = _AGENT
_AGENTCONTAINER.fields_by_name['entries'].message_type = _AGENT
DESCRIPTOR.message_types_by_name['Agent'] = _AGENT
DESCRIPTOR.message_types_by_name['AgentContainer'] = _AGENTCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Agent = _reflection.GeneratedProtocolMessageType('Agent', (_message.Message,), {
  'DESCRIPTOR' : _AGENT,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:Agent)
  })
_sym_db.RegisterMessage(Agent)

AgentContainer = _reflection.GeneratedProtocolMessageType('AgentContainer', (_message.Message,), {
  'DESCRIPTOR' : _AGENTCONTAINER,
  '__module__' : 'agent_pb2'
  # @@protoc_insertion_point(class_scope:AgentContainer)
  })
_sym_db.RegisterMessage(AgentContainer)


# @@protoc_insertion_point(module_scope)
