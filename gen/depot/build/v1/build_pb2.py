# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: depot/build/v1/build.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x64\x65pot/build/v1/build.proto\x12\x0e\x64\x65pot.build.v1\"3\n\x12\x43reateBuildRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"Q\n\x13\x43reateBuildResponse\x12\x19\n\x08\x62uild_id\x18\x01 \x01(\tR\x07\x62uildId\x12\x1f\n\x0b\x62uild_token\x18\x02 \x01(\tR\nbuildToken\"\x81\x02\n\x12\x46inishBuildRequest\x12\x19\n\x08\x62uild_id\x18\x01 \x01(\tR\x07\x62uildId\x12K\n\x07success\x18\x02 \x01(\x0b\x32/.depot.build.v1.FinishBuildRequest.BuildSuccessH\x00R\x07success\x12\x45\n\x05\x65rror\x18\x03 \x01(\x0b\x32-.depot.build.v1.FinishBuildRequest.BuildErrorH\x00R\x05\x65rror\x1a\x0e\n\x0c\x42uildSuccess\x1a\"\n\nBuildError\x12\x14\n\x05\x65rror\x18\x01 \x01(\tR\x05\x65rrorB\x08\n\x06result\"\x15\n\x13\x46inishBuildResponse2\xbe\x01\n\x0c\x42uildService\x12V\n\x0b\x43reateBuild\x12\".depot.build.v1.CreateBuildRequest\x1a#.depot.build.v1.CreateBuildResponse\x12V\n\x0b\x46inishBuild\x12\".depot.build.v1.FinishBuildRequest\x1a#.depot.build.v1.FinishBuildResponseBz\n\x12\x63om.depot.build.v1B\nBuildProtoP\x01\xa2\x02\x03\x44\x42X\xaa\x02\x0e\x44\x65pot.Build.V1\xca\x02\x0e\x44\x65pot\\Build\\V1\xe2\x02\x1a\x44\x65pot\\Build\\V1\\GPBMetadata\xea\x02\x10\x44\x65pot::Build::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'depot.build.v1.build_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.depot.build.v1B\nBuildProtoP\001\242\002\003DBX\252\002\016Depot.Build.V1\312\002\016Depot\\Build\\V1\342\002\032Depot\\Build\\V1\\GPBMetadata\352\002\020Depot::Build::V1'
  _globals['_CREATEBUILDREQUEST']._serialized_start=46
  _globals['_CREATEBUILDREQUEST']._serialized_end=97
  _globals['_CREATEBUILDRESPONSE']._serialized_start=99
  _globals['_CREATEBUILDRESPONSE']._serialized_end=180
  _globals['_FINISHBUILDREQUEST']._serialized_start=183
  _globals['_FINISHBUILDREQUEST']._serialized_end=440
  _globals['_FINISHBUILDREQUEST_BUILDSUCCESS']._serialized_start=380
  _globals['_FINISHBUILDREQUEST_BUILDSUCCESS']._serialized_end=394
  _globals['_FINISHBUILDREQUEST_BUILDERROR']._serialized_start=396
  _globals['_FINISHBUILDREQUEST_BUILDERROR']._serialized_end=430
  _globals['_FINISHBUILDRESPONSE']._serialized_start=442
  _globals['_FINISHBUILDRESPONSE']._serialized_end=463
  _globals['_BUILDSERVICE']._serialized_start=466
  _globals['_BUILDSERVICE']._serialized_end=656
# @@protoc_insertion_point(module_scope)
