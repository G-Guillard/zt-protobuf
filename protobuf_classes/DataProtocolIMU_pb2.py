# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DataProtocolIMU.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='DataProtocolIMU.proto',
  package='com.michelin.bib.protocol',
  syntax='proto2',
  serialized_options=b'\n\031com.michelin.bib.protocolB\017DataProtocolIMU',
  serialized_pb=b'\n\x15\x44\x61taProtocolIMU.proto\x12\x19\x63om.michelin.bib.protocol\"A\n\x06Header\x12\x11\n\tdayNumber\x18\x01 \x02(\r\x12\x11\n\tIMEIpart1\x18\x02 \x02(\r\x12\x11\n\tIMEIpart2\x18\x03 \x02(\r\"V\n\x0fSynchronisation\x12\x31\n\x06header\x18\x01 \x02(\x0b\x32!.com.michelin.bib.protocol.Header\x12\x10\n\x08nbMillis\x18\x02 \x02(\r\"\xaa\x02\n\rCommunication\x12\x41\n\x07\x63ommand\x18\x03 \x01(\x0e\x32\x30.com.michelin.bib.protocol.Communication.Command\x12\x0c\n\x04\x61rgs\x18\x04 \x03(\t\"\xc7\x01\n\x07\x43ommand\x12\x0c\n\x08\x44\x45\x42UG_ON\x10\x00\x12\r\n\tDEBUG_OFF\x10\x01\x12\t\n\x05RESET\x10\x02\x12\r\n\tIS_SYNCED\x10\x03\x12\x07\n\x03RTC\x10\x04\x12\x10\n\x0cMILLISECONDS\x10\x05\x12\x10\n\x0cMICROSECONDS\x10\x06\x12\r\n\tFAKE_SYNC\x10\x07\x12\x08\n\x04\x42\x41RK\x10\x08\x12\x1b\n\x17LAST_ACCELEROMETER_DATA\x10\t\x12\x17\n\x13LAST_ALTIMETER_DATA\x10\n\x12\t\n\x05\x41\x42OUT\x10\x0b\"\xdf\x01\n\rAccelerometer\x12\x16\n\x0e\x66irstTimestamp\x18\x01 \x02(\r\x12\x15\n\rlastTimestamp\x18\x02 \x02(\r\x12\x0e\n\x02\x61x\x18\x03 \x03(\x11\x42\x02\x10\x01\x12\x0e\n\x02\x61y\x18\x04 \x03(\x11\x42\x02\x10\x01\x12\x0e\n\x02\x61z\x18\x05 \x03(\x11\x42\x02\x10\x01\x12\x0e\n\x02gx\x18\x06 \x03(\x11\x42\x02\x10\x01\x12\x0e\n\x02gy\x18\x07 \x03(\x11\x42\x02\x10\x01\x12\x0e\n\x02gz\x18\x08 \x03(\x11\x42\x02\x10\x01\x12\x0e\n\x02mx\x18\t \x03(\x11\x42\x02\x10\x01\x12\x0e\n\x02my\x18\n \x03(\x11\x42\x02\x10\x01\x12\x0e\n\x02mz\x18\x0b \x03(\x11\x42\x02\x10\x01\x12\x0f\n\x07isShock\x18\x0c \x01(\x08\"Q\n\tAltimeter\x12\x15\n\ttimestamp\x18\x01 \x03(\rB\x02\x10\x01\x12\x17\n\x0btemperature\x18\x02 \x03(\rB\x02\x10\x01\x12\x14\n\x08pressure\x18\x03 \x03(\rB\x02\x10\x01\"\xbd\x01\n\x13ProtocolMessagesIMU\x12\x31\n\x06header\x18\x01 \x02(\x0b\x32!.com.michelin.bib.protocol.Header\x12\x37\n\taltimeter\x18\x05 \x03(\x0b\x32$.com.michelin.bib.protocol.Altimeter\x12:\n\x08\x61\x63\x63\x65lero\x18\x06 \x03(\x0b\x32(.com.michelin.bib.protocol.AccelerometerB,\n\x19\x63om.michelin.bib.protocolB\x0f\x44\x61taProtocolIMU'
)



_COMMUNICATION_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='com.michelin.bib.protocol.Communication.Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEBUG_ON', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBUG_OFF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IS_SYNCED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTC', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MILLISECONDS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MICROSECONDS', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAKE_SYNC', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BARK', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_ACCELEROMETER_DATA', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_ALTIMETER_DATA', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABOUT', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=307,
  serialized_end=506,
)
_sym_db.RegisterEnumDescriptor(_COMMUNICATION_COMMAND)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='com.michelin.bib.protocol.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dayNumber', full_name='com.michelin.bib.protocol.Header.dayNumber', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='IMEIpart1', full_name='com.michelin.bib.protocol.Header.IMEIpart1', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='IMEIpart2', full_name='com.michelin.bib.protocol.Header.IMEIpart2', index=2,
      number=3, type=13, cpp_type=3, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=117,
)


_SYNCHRONISATION = _descriptor.Descriptor(
  name='Synchronisation',
  full_name='com.michelin.bib.protocol.Synchronisation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.michelin.bib.protocol.Synchronisation.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nbMillis', full_name='com.michelin.bib.protocol.Synchronisation.nbMillis', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=205,
)


_COMMUNICATION = _descriptor.Descriptor(
  name='Communication',
  full_name='com.michelin.bib.protocol.Communication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='com.michelin.bib.protocol.Communication.command', index=0,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='com.michelin.bib.protocol.Communication.args', index=1,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMUNICATION_COMMAND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=506,
)


_ACCELEROMETER = _descriptor.Descriptor(
  name='Accelerometer',
  full_name='com.michelin.bib.protocol.Accelerometer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firstTimestamp', full_name='com.michelin.bib.protocol.Accelerometer.firstTimestamp', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastTimestamp', full_name='com.michelin.bib.protocol.Accelerometer.lastTimestamp', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ax', full_name='com.michelin.bib.protocol.Accelerometer.ax', index=2,
      number=3, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ay', full_name='com.michelin.bib.protocol.Accelerometer.ay', index=3,
      number=4, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='az', full_name='com.michelin.bib.protocol.Accelerometer.az', index=4,
      number=5, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gx', full_name='com.michelin.bib.protocol.Accelerometer.gx', index=5,
      number=6, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gy', full_name='com.michelin.bib.protocol.Accelerometer.gy', index=6,
      number=7, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gz', full_name='com.michelin.bib.protocol.Accelerometer.gz', index=7,
      number=8, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mx', full_name='com.michelin.bib.protocol.Accelerometer.mx', index=8,
      number=9, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='my', full_name='com.michelin.bib.protocol.Accelerometer.my', index=9,
      number=10, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mz', full_name='com.michelin.bib.protocol.Accelerometer.mz', index=10,
      number=11, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isShock', full_name='com.michelin.bib.protocol.Accelerometer.isShock', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=732,
)


_ALTIMETER = _descriptor.Descriptor(
  name='Altimeter',
  full_name='com.michelin.bib.protocol.Altimeter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='com.michelin.bib.protocol.Altimeter.timestamp', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='com.michelin.bib.protocol.Altimeter.temperature', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pressure', full_name='com.michelin.bib.protocol.Altimeter.pressure', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\020\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=734,
  serialized_end=815,
)


_PROTOCOLMESSAGESIMU = _descriptor.Descriptor(
  name='ProtocolMessagesIMU',
  full_name='com.michelin.bib.protocol.ProtocolMessagesIMU',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='com.michelin.bib.protocol.ProtocolMessagesIMU.header', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altimeter', full_name='com.michelin.bib.protocol.ProtocolMessagesIMU.altimeter', index=1,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accelero', full_name='com.michelin.bib.protocol.ProtocolMessagesIMU.accelero', index=2,
      number=6, type=11, cpp_type=10, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=818,
  serialized_end=1007,
)

_SYNCHRONISATION.fields_by_name['header'].message_type = _HEADER
_COMMUNICATION.fields_by_name['command'].enum_type = _COMMUNICATION_COMMAND
_COMMUNICATION_COMMAND.containing_type = _COMMUNICATION
_PROTOCOLMESSAGESIMU.fields_by_name['header'].message_type = _HEADER
_PROTOCOLMESSAGESIMU.fields_by_name['altimeter'].message_type = _ALTIMETER
_PROTOCOLMESSAGESIMU.fields_by_name['accelero'].message_type = _ACCELEROMETER
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Synchronisation'] = _SYNCHRONISATION
DESCRIPTOR.message_types_by_name['Communication'] = _COMMUNICATION
DESCRIPTOR.message_types_by_name['Accelerometer'] = _ACCELEROMETER
DESCRIPTOR.message_types_by_name['Altimeter'] = _ALTIMETER
DESCRIPTOR.message_types_by_name['ProtocolMessagesIMU'] = _PROTOCOLMESSAGESIMU
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), {
  'DESCRIPTOR' : _HEADER,
  '__module__' : 'DataProtocolIMU_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.protocol.Header)
  })
_sym_db.RegisterMessage(Header)

Synchronisation = _reflection.GeneratedProtocolMessageType('Synchronisation', (_message.Message,), {
  'DESCRIPTOR' : _SYNCHRONISATION,
  '__module__' : 'DataProtocolIMU_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.protocol.Synchronisation)
  })
_sym_db.RegisterMessage(Synchronisation)

Communication = _reflection.GeneratedProtocolMessageType('Communication', (_message.Message,), {
  'DESCRIPTOR' : _COMMUNICATION,
  '__module__' : 'DataProtocolIMU_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.protocol.Communication)
  })
_sym_db.RegisterMessage(Communication)

Accelerometer = _reflection.GeneratedProtocolMessageType('Accelerometer', (_message.Message,), {
  'DESCRIPTOR' : _ACCELEROMETER,
  '__module__' : 'DataProtocolIMU_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.protocol.Accelerometer)
  })
_sym_db.RegisterMessage(Accelerometer)

Altimeter = _reflection.GeneratedProtocolMessageType('Altimeter', (_message.Message,), {
  'DESCRIPTOR' : _ALTIMETER,
  '__module__' : 'DataProtocolIMU_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.protocol.Altimeter)
  })
_sym_db.RegisterMessage(Altimeter)

ProtocolMessagesIMU = _reflection.GeneratedProtocolMessageType('ProtocolMessagesIMU', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOLMESSAGESIMU,
  '__module__' : 'DataProtocolIMU_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.protocol.ProtocolMessagesIMU)
  })
_sym_db.RegisterMessage(ProtocolMessagesIMU)


DESCRIPTOR._options = None
_ACCELEROMETER.fields_by_name['ax']._options = None
_ACCELEROMETER.fields_by_name['ay']._options = None
_ACCELEROMETER.fields_by_name['az']._options = None
_ACCELEROMETER.fields_by_name['gx']._options = None
_ACCELEROMETER.fields_by_name['gy']._options = None
_ACCELEROMETER.fields_by_name['gz']._options = None
_ACCELEROMETER.fields_by_name['mx']._options = None
_ACCELEROMETER.fields_by_name['my']._options = None
_ACCELEROMETER.fields_by_name['mz']._options = None
_ALTIMETER.fields_by_name['timestamp']._options = None
_ALTIMETER.fields_by_name['temperature']._options = None
_ALTIMETER.fields_by_name['pressure']._options = None
# @@protoc_insertion_point(module_scope)
