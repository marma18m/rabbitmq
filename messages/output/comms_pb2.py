# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages/comms.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x14messages/comms.proto\x12\x08tutorial\"\xbc\x01\n\x0c\x43ommsMessage\x12\x11\n\ttimestamp\x18\x01 \x02(\x03\x12\x38\n\x0c\x63\x61mera_specs\x18\x02 \x01(\x0b\x32\".tutorial.CommsMessage.CameraSpecs\x12\x12\n\nprediction\x18\x03 \x02(\t\x12\x0e\n\x06\x61\x63tion\x18\x04 \x02(\t\x1a;\n\x0b\x43\x61meraSpecs\x12\x15\n\rcamera_spec_1\x18\x01 \x01(\t\x12\x15\n\rcamera_spec_2\x18\x02 \x01(\x05'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, 'messages.comms_pb2', globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _COMMSMESSAGE._serialized_start = 35
    _COMMSMESSAGE._serialized_end = 223
    _COMMSMESSAGE_CAMERASPECS._serialized_start = 164
    _COMMSMESSAGE_CAMERASPECS._serialized_end = 223
# @@protoc_insertion_point(module_scope)
