# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rv2/protos/make_train_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rv2.protos import machine_learning_pb2 as rv2_dot_protos_dot_machine__learning__pb2
from rv2.protos import raster_transformer_pb2 as rv2_dot_protos_dot_raster__transformer__pb2
from rv2.protos import raster_source_pb2 as rv2_dot_protos_dot_raster__source__pb2
from rv2.protos import annotation_source_pb2 as rv2_dot_protos_dot_annotation__source__pb2
from rv2.protos import label_item_pb2 as rv2_dot_protos_dot_label__item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rv2/protos/make_train_data.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_pb=_b('\n rv2/protos/make_train_data.proto\x12\trv.protos\x1a!rv2/protos/machine_learning.proto\x1a#rv2/protos/raster_transformer.proto\x1a\x1erv2/protos/raster_source.proto\x1a\"rv2/protos/annotation_source.proto\x1a\x1brv2/protos/label_item.proto\"\xd5\x05\n\rMakeTrainData\x12\x38\n\x0etrain_projects\x18\x01 \x03(\x0b\x32 .rv.protos.MakeTrainData.Project\x12=\n\x13validation_projects\x18\x02 \x03(\x0b\x32 .rv.protos.MakeTrainData.Project\x12\x34\n\x10machine_learning\x18\x03 \x02(\x0b\x32\x1a.rv.protos.MachineLearning\x12\x31\n\x07options\x18\x04 \x02(\x0b\x32 .rv.protos.MakeTrainData.Options\x12)\n\x0blabel_items\x18\x05 \x03(\x0b\x32\x14.rv.protos.LabelItem\x1aq\n\x07Project\x12.\n\rraster_source\x18\x01 \x02(\x0b\x32\x17.rv.protos.RasterSource\x12\x36\n\x11\x61nnotation_source\x18\x02 \x02(\x0b\x32\x1b.rv.protos.AnnotationSource\x1aZ\n\x16ObjectDetectionOptions\x12\x11\n\tneg_ratio\x18\x01 \x02(\x02\x12\x17\n\nioa_thresh\x18\x02 \x01(\x02:\x03\x30.8\x12\x14\n\x0csingle_label\x18\x03 \x01(\t\x1a\xe7\x01\n\x07Options\x12\x11\n\tchip_size\x18\x01 \x02(\x05\x12\x38\n\x12raster_transformer\x18\x02 \x02(\x0b\x32\x1c.rv.protos.RasterTransformer\x12\x13\n\x05\x64\x65\x62ug\x18\x03 \x01(\x08:\x04true\x12\x12\n\noutput_uri\x18\x04 \x02(\t\x12S\n\x18object_detection_options\x18\x05 \x01(\x0b\x32/.rv.protos.MakeTrainData.ObjectDetectionOptionsH\x00\x42\x11\n\x0fml_options_type')
  ,
  dependencies=[rv2_dot_protos_dot_machine__learning__pb2.DESCRIPTOR,rv2_dot_protos_dot_raster__transformer__pb2.DESCRIPTOR,rv2_dot_protos_dot_raster__source__pb2.DESCRIPTOR,rv2_dot_protos_dot_annotation__source__pb2.DESCRIPTOR,rv2_dot_protos_dot_label__item__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MAKETRAINDATA_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='rv.protos.MakeTrainData.Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raster_source', full_name='rv.protos.MakeTrainData.Project.raster_source', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='annotation_source', full_name='rv.protos.MakeTrainData.Project.annotation_source', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=616,
)

_MAKETRAINDATA_OBJECTDETECTIONOPTIONS = _descriptor.Descriptor(
  name='ObjectDetectionOptions',
  full_name='rv.protos.MakeTrainData.ObjectDetectionOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='neg_ratio', full_name='rv.protos.MakeTrainData.ObjectDetectionOptions.neg_ratio', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ioa_thresh', full_name='rv.protos.MakeTrainData.ObjectDetectionOptions.ioa_thresh', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.8),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='single_label', full_name='rv.protos.MakeTrainData.ObjectDetectionOptions.single_label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=618,
  serialized_end=708,
)

_MAKETRAINDATA_OPTIONS = _descriptor.Descriptor(
  name='Options',
  full_name='rv.protos.MakeTrainData.Options',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chip_size', full_name='rv.protos.MakeTrainData.Options.chip_size', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raster_transformer', full_name='rv.protos.MakeTrainData.Options.raster_transformer', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug', full_name='rv.protos.MakeTrainData.Options.debug', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_uri', full_name='rv.protos.MakeTrainData.Options.output_uri', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_detection_options', full_name='rv.protos.MakeTrainData.Options.object_detection_options', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ml_options_type', full_name='rv.protos.MakeTrainData.Options.ml_options_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=711,
  serialized_end=942,
)

_MAKETRAINDATA = _descriptor.Descriptor(
  name='MakeTrainData',
  full_name='rv.protos.MakeTrainData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='train_projects', full_name='rv.protos.MakeTrainData.train_projects', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validation_projects', full_name='rv.protos.MakeTrainData.validation_projects', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='machine_learning', full_name='rv.protos.MakeTrainData.machine_learning', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='options', full_name='rv.protos.MakeTrainData.options', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label_items', full_name='rv.protos.MakeTrainData.label_items', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MAKETRAINDATA_PROJECT, _MAKETRAINDATA_OBJECTDETECTIONOPTIONS, _MAKETRAINDATA_OPTIONS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=942,
)

_MAKETRAINDATA_PROJECT.fields_by_name['raster_source'].message_type = rv2_dot_protos_dot_raster__source__pb2._RASTERSOURCE
_MAKETRAINDATA_PROJECT.fields_by_name['annotation_source'].message_type = rv2_dot_protos_dot_annotation__source__pb2._ANNOTATIONSOURCE
_MAKETRAINDATA_PROJECT.containing_type = _MAKETRAINDATA
_MAKETRAINDATA_OBJECTDETECTIONOPTIONS.containing_type = _MAKETRAINDATA
_MAKETRAINDATA_OPTIONS.fields_by_name['raster_transformer'].message_type = rv2_dot_protos_dot_raster__transformer__pb2._RASTERTRANSFORMER
_MAKETRAINDATA_OPTIONS.fields_by_name['object_detection_options'].message_type = _MAKETRAINDATA_OBJECTDETECTIONOPTIONS
_MAKETRAINDATA_OPTIONS.containing_type = _MAKETRAINDATA
_MAKETRAINDATA_OPTIONS.oneofs_by_name['ml_options_type'].fields.append(
  _MAKETRAINDATA_OPTIONS.fields_by_name['object_detection_options'])
_MAKETRAINDATA_OPTIONS.fields_by_name['object_detection_options'].containing_oneof = _MAKETRAINDATA_OPTIONS.oneofs_by_name['ml_options_type']
_MAKETRAINDATA.fields_by_name['train_projects'].message_type = _MAKETRAINDATA_PROJECT
_MAKETRAINDATA.fields_by_name['validation_projects'].message_type = _MAKETRAINDATA_PROJECT
_MAKETRAINDATA.fields_by_name['machine_learning'].message_type = rv2_dot_protos_dot_machine__learning__pb2._MACHINELEARNING
_MAKETRAINDATA.fields_by_name['options'].message_type = _MAKETRAINDATA_OPTIONS
_MAKETRAINDATA.fields_by_name['label_items'].message_type = rv2_dot_protos_dot_label__item__pb2._LABELITEM
DESCRIPTOR.message_types_by_name['MakeTrainData'] = _MAKETRAINDATA

MakeTrainData = _reflection.GeneratedProtocolMessageType('MakeTrainData', (_message.Message,), dict(

  Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), dict(
    DESCRIPTOR = _MAKETRAINDATA_PROJECT,
    __module__ = 'rv2.protos.make_train_data_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.MakeTrainData.Project)
    ))
  ,

  ObjectDetectionOptions = _reflection.GeneratedProtocolMessageType('ObjectDetectionOptions', (_message.Message,), dict(
    DESCRIPTOR = _MAKETRAINDATA_OBJECTDETECTIONOPTIONS,
    __module__ = 'rv2.protos.make_train_data_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.MakeTrainData.ObjectDetectionOptions)
    ))
  ,

  Options = _reflection.GeneratedProtocolMessageType('Options', (_message.Message,), dict(
    DESCRIPTOR = _MAKETRAINDATA_OPTIONS,
    __module__ = 'rv2.protos.make_train_data_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.MakeTrainData.Options)
    ))
  ,
  DESCRIPTOR = _MAKETRAINDATA,
  __module__ = 'rv2.protos.make_train_data_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.MakeTrainData)
  ))
_sym_db.RegisterMessage(MakeTrainData)
_sym_db.RegisterMessage(MakeTrainData.Project)
_sym_db.RegisterMessage(MakeTrainData.ObjectDetectionOptions)
_sym_db.RegisterMessage(MakeTrainData.Options)


# @@protoc_insertion_point(module_scope)
