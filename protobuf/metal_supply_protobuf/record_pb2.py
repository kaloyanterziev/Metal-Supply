# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metal_supply_protobuf/record.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='metal_supply_protobuf/record.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\"metal_supply_protobuf/record.proto\"\xba\x03\n\x06Record\x12\x11\n\trecord_id\x18\x01 \x01(\t\x12\x17\n\x0fnext_record_ids\x18\x02 \x03(\t\x12\x1d\n\x06owners\x18\x03 \x03(\x0b\x32\r.Record.Owner\x12\x15\n\rmaterial_type\x18\x04 \x01(\t\x12\x17\n\x0fmaterial_origin\x18\x05 \x01(\t\x12\x0e\n\x06tonnes\x18\x06 \x01(\x01\x12!\n\x08\x63ontents\x18\x07 \x03(\x0b\x32\x0f.Record.Content\x12#\n\tlocations\x18\x08 \x03(\x0b\x32\x10.Record.Location\x12\x11\n\ttimestamp\x18\t \x01(\x04\x1a\x46\n\x05Owner\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\t\x12\x18\n\x10percentage_owner\x18\x02 \x01(\x01\x12\x11\n\ttimestamp\x18\x03 \x01(\x04\x1aT\n\x08Location\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08\x61gent_id\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\x1a,\n\x07\x43ontent\x12\r\n\x05metal\x18\x01 \x01(\t\x12\x12\n\npercentage\x18\x02 \x01(\x01\"+\n\x0fRecordContainer\x12\x18\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x07.Recordb\x06proto3'
)




_RECORD_OWNER = _descriptor.Descriptor(
  name='Owner',
  full_name='Record.Owner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='Record.Owner.agent_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percentage_owner', full_name='Record.Owner.percentage_owner', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Record.Owner.timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=279,
  serialized_end=349,
)

_RECORD_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='Record.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Record.Location.latitude', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Record.Location.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_id', full_name='Record.Location.agent_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Record.Location.timestamp', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=351,
  serialized_end=435,
)

_RECORD_CONTENT = _descriptor.Descriptor(
  name='Content',
  full_name='Record.Content',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metal', full_name='Record.Content.metal', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percentage', full_name='Record.Content.percentage', index=1,
      number=2, type=1, cpp_type=5, label=1,
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
  serialized_start=437,
  serialized_end=481,
)

_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_id', full_name='Record.record_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_record_ids', full_name='Record.next_record_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owners', full_name='Record.owners', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='material_type', full_name='Record.material_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='material_origin', full_name='Record.material_origin', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tonnes', full_name='Record.tonnes', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents', full_name='Record.contents', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locations', full_name='Record.locations', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Record.timestamp', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_RECORD_OWNER, _RECORD_LOCATION, _RECORD_CONTENT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=481,
)


_RECORDCONTAINER = _descriptor.Descriptor(
  name='RecordContainer',
  full_name='RecordContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='RecordContainer.entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=526,
)

_RECORD_OWNER.containing_type = _RECORD
_RECORD_LOCATION.containing_type = _RECORD
_RECORD_CONTENT.containing_type = _RECORD
_RECORD.fields_by_name['owners'].message_type = _RECORD_OWNER
_RECORD.fields_by_name['contents'].message_type = _RECORD_CONTENT
_RECORD.fields_by_name['locations'].message_type = _RECORD_LOCATION
_RECORDCONTAINER.fields_by_name['entries'].message_type = _RECORD
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['RecordContainer'] = _RECORDCONTAINER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {

  'Owner' : _reflection.GeneratedProtocolMessageType('Owner', (_message.Message,), {
    'DESCRIPTOR' : _RECORD_OWNER,
    '__module__' : 'metal_supply_protobuf.record_pb2'
    # @@protoc_insertion_point(class_scope:Record.Owner)
    })
  ,

  'Location' : _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
    'DESCRIPTOR' : _RECORD_LOCATION,
    '__module__' : 'metal_supply_protobuf.record_pb2'
    # @@protoc_insertion_point(class_scope:Record.Location)
    })
  ,

  'Content' : _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), {
    'DESCRIPTOR' : _RECORD_CONTENT,
    '__module__' : 'metal_supply_protobuf.record_pb2'
    # @@protoc_insertion_point(class_scope:Record.Content)
    })
  ,
  'DESCRIPTOR' : _RECORD,
  '__module__' : 'metal_supply_protobuf.record_pb2'
  # @@protoc_insertion_point(class_scope:Record)
  })
_sym_db.RegisterMessage(Record)
_sym_db.RegisterMessage(Record.Owner)
_sym_db.RegisterMessage(Record.Location)
_sym_db.RegisterMessage(Record.Content)

RecordContainer = _reflection.GeneratedProtocolMessageType('RecordContainer', (_message.Message,), {
  'DESCRIPTOR' : _RECORDCONTAINER,
  '__module__' : 'metal_supply_protobuf.record_pb2'
  # @@protoc_insertion_point(class_scope:RecordContainer)
  })
_sym_db.RegisterMessage(RecordContainer)


# @@protoc_insertion_point(module_scope)
