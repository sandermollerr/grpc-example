# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ns/grpc/protobufs/lang_detection/lang-detection.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5ns/grpc/protobufs/lang_detection/lang-detection.proto\"5\n\x10LangModelRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\x05\".\n\x0fLangModelResult\x12\x0c\n\x04lang\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\"6\n\x11LangModelResponse\x12!\n\x07results\x18\x01 \x03(\x0b\x32\x10.LangModelResult2C\n\x10LanguageDetector\x12/\n\x06\x64\x65tect\x12\x11.LangModelRequest\x1a\x12.LangModelResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ns.grpc.protobufs.lang_detection.lang_detection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LANGMODELREQUEST']._serialized_start=57
  _globals['_LANGMODELREQUEST']._serialized_end=110
  _globals['_LANGMODELRESULT']._serialized_start=112
  _globals['_LANGMODELRESULT']._serialized_end=158
  _globals['_LANGMODELRESPONSE']._serialized_start=160
  _globals['_LANGMODELRESPONSE']._serialized_end=214
  _globals['_LANGUAGEDETECTOR']._serialized_start=216
  _globals['_LANGUAGEDETECTOR']._serialized_end=283
# @@protoc_insertion_point(module_scope)