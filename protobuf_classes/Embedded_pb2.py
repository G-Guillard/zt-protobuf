# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Embedded.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Embedded.proto',
  package='com.michelin.bib.embedded',
  syntax='proto2',
  serialized_options=b'\n\031com.michelin.bib.embeddedB\010Embedded',
  serialized_pb=b'\n\x0e\x45mbedded.proto\x12\x19\x63om.michelin.bib.embedded\x1a google/protobuf/descriptor.proto\"\xb3\x06\n\rVSPOutputData\x12\x0c\n\x04time\x18\x01 \x02(\r\x12\x1d\n\x15referenceEngineTorque\x18\x02 \x02(\x01\x12\x1a\n\x12secondaryAxleRatio\x18\x03 \x02(\x01\x12\x12\n\ntireRadius\x18\x04 \x02(\x01\x12+\n#referenceEngineTorqueLearningNumber\x18\x05 \x02(\x01\x12(\n secondaryAxleRatioLearningNumber\x18\x06 \x02(\x01\x12I\n\x10\x61vailableSignals\x18\x07 \x03(\x0e\x32/.com.michelin.bib.embedded.VSPOutputData.Signal\"\xa2\x04\n\x06Signal\x12\x12\n\x0e\x46rontAxleSpeed\x10\x00\x12\x0f\n\x0b\x45ngineSpeed\x10\x01\x12$\n DriverSDemandEnginePercentTorque\x10\x02\x12\x1d\n\x19\x41\x63tualEnginePercentTorque\x10\x03\x12 \n\x1cNominalFrictionPercentTorque\x10\x04\x12\x12\n\x0e\x45ngineFuelRate\x10\x05\x12%\n!HighResolutionEngineTotalFuelUsed\x10\x06\x12\x1c\n\x18\x45ngineCoolantTemperature\x10\x07\x12\x19\n\x15\x45ngineOilTemperature1\x10\x08\x12\x1f\n\x1b\x41\x63tualRetarderPercentTorque\x10\t\x12\x16\n\x12\x42rakePedalPosition\x10\n\x12\x0f\n\x0b\x42rakeSwitch\x10\x0b\x12\x1f\n\x1bTransmissionInputShaftSpeed\x10\x0c\x12\x1c\n\x18TransmissionSelectedGear\x10\r\x12\x1b\n\x17TransmissionCurrentGear\x10\x0e\x12\x1f\n\x1bTransmissionActualGearRatio\x10\x0f\x12\x13\n\x0fSteerWheelAngle\x10\x10\x12\x19\n\x15SteerWheelTurnCounter\x10\x11\x12!\n\x1dGrossCombinationVehicleWeight\x10\x12\"\x86\x01\n\x10VSPOutputSignals\x12\x0c\n\x04time\x18\x01 \x03(\r\x12\x17\n\x0fvehicleSpeedKmh\x18\x02 \x03(\r\x12\x16\n\x0e\x65ngineSpeedRpm\x18\x03 \x03(\r\x12\x1f\n\x17\x65ngineEffectiveTorqueNm\x18\x04 \x03(\x05\x12\x12\n\ngearNumber\x18\x05 \x03(\r\"B\n\x12GVWEstimatorOutput\x12\x0c\n\x04time\x18\x01 \x02(\r\x12\x0f\n\x07gvw_est\x18\x02 \x02(\x02\x12\r\n\x05sigma\x18\x03 \x02(\x02\"\xd4\x01\n\x19\x45\x63oDrivingEstimatorOutput\x12\r\n\x05t_ini\x18\x01 \x03(\x01\x12\r\n\x05t_end\x18\x02 \x03(\x01\x12G\n\x04type\x18\x03 \x03(\x0e\x32\x39.com.michelin.bib.embedded.EcoDrivingEstimatorOutput.Type\"P\n\x04Type\x12\x07\n\x03Nul\x10\x00\x12\x08\n\x04Stop\x10\x01\x12\x0e\n\nTrafficJam\x10\x02\x12\x08\n\x04\x46ree\x10\x03\x12\x08\n\x04Turn\x10\x04\x12\x11\n\rTrafficCircle\x10\x05\"\xbf\x03\n\x18\x45nergeticDiagnosisOutput\x12\x0c\n\x04time\x18\x01 \x02(\r\x12\x18\n\x10\x66uelConsumptionL\x18\x02 \x03(\x01\x12\x1a\n\x12indicatedEnergykWh\x18\x03 \x03(\x01\x12\x19\n\x11\x66rictionEnergykWh\x18\x04 \x03(\x01\x12\x1a\n\x12\x65\x66\x66\x65\x63tiveEnergykWh\x18\x05 \x03(\x01\x12\x1b\n\x13\x64istanceTransGearKm\x18\x06 \x03(\x01\x12\x1c\n\x14\x64urationClutchStateS\x18\x07 \x03(\x01\x12\x1a\n\x12\x64urationTransGearS\x18\x08 \x03(\x01\x12!\n\x19\x64istancePowertrainStateKm\x18\t \x03(\x01\x12 \n\x18\x64urationPowertrainStateS\x18\n \x03(\x01\x12\x1d\n\x15\x64istanceClutchStateKm\x18\x0b \x03(\x01\x12\x1c\n\x14\x61uxiliariesEnergykWh\x18\x0c \x03(\x01\x12\x1d\n\x15powerTakeOffEnergykWh\x18\r \x02(\x01\x12\x18\n\x10primaryEnergykWh\x18\x0e \x03(\x01\x12\x16\n\x0ewheelEnergykWh\x18\x0f \x03(\x01\x42%\n\x19\x63om.michelin.bib.embeddedB\x08\x45mbedded'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])



_VSPOUTPUTDATA_SIGNAL = _descriptor.EnumDescriptor(
  name='Signal',
  full_name='com.michelin.bib.embedded.VSPOutputData.Signal',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FrontAxleSpeed', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EngineSpeed', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DriverSDemandEnginePercentTorque', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActualEnginePercentTorque', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NominalFrictionPercentTorque', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EngineFuelRate', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HighResolutionEngineTotalFuelUsed', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EngineCoolantTemperature', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EngineOilTemperature1', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ActualRetarderPercentTorque', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BrakePedalPosition', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BrakeSwitch', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TransmissionInputShaftSpeed', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TransmissionSelectedGear', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TransmissionCurrentGear', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TransmissionActualGearRatio', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SteerWheelAngle', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SteerWheelTurnCounter', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GrossCombinationVehicleWeight', index=18, number=18,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=353,
  serialized_end=899,
)
_sym_db.RegisterEnumDescriptor(_VSPOUTPUTDATA_SIGNAL)

_ECODRIVINGESTIMATOROUTPUT_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='com.michelin.bib.embedded.EcoDrivingEstimatorOutput.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Nul', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Stop', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TrafficJam', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Free', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Turn', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TrafficCircle', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1239,
  serialized_end=1319,
)
_sym_db.RegisterEnumDescriptor(_ECODRIVINGESTIMATOROUTPUT_TYPE)


_VSPOUTPUTDATA = _descriptor.Descriptor(
  name='VSPOutputData',
  full_name='com.michelin.bib.embedded.VSPOutputData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.michelin.bib.embedded.VSPOutputData.time', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenceEngineTorque', full_name='com.michelin.bib.embedded.VSPOutputData.referenceEngineTorque', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondaryAxleRatio', full_name='com.michelin.bib.embedded.VSPOutputData.secondaryAxleRatio', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tireRadius', full_name='com.michelin.bib.embedded.VSPOutputData.tireRadius', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenceEngineTorqueLearningNumber', full_name='com.michelin.bib.embedded.VSPOutputData.referenceEngineTorqueLearningNumber', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondaryAxleRatioLearningNumber', full_name='com.michelin.bib.embedded.VSPOutputData.secondaryAxleRatioLearningNumber', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='availableSignals', full_name='com.michelin.bib.embedded.VSPOutputData.availableSignals', index=6,
      number=7, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VSPOUTPUTDATA_SIGNAL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=899,
)


_VSPOUTPUTSIGNALS = _descriptor.Descriptor(
  name='VSPOutputSignals',
  full_name='com.michelin.bib.embedded.VSPOutputSignals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.michelin.bib.embedded.VSPOutputSignals.time', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicleSpeedKmh', full_name='com.michelin.bib.embedded.VSPOutputSignals.vehicleSpeedKmh', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engineSpeedRpm', full_name='com.michelin.bib.embedded.VSPOutputSignals.engineSpeedRpm', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engineEffectiveTorqueNm', full_name='com.michelin.bib.embedded.VSPOutputSignals.engineEffectiveTorqueNm', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gearNumber', full_name='com.michelin.bib.embedded.VSPOutputSignals.gearNumber', index=4,
      number=5, type=13, cpp_type=3, label=3,
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
  serialized_start=902,
  serialized_end=1036,
)


_GVWESTIMATOROUTPUT = _descriptor.Descriptor(
  name='GVWEstimatorOutput',
  full_name='com.michelin.bib.embedded.GVWEstimatorOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.michelin.bib.embedded.GVWEstimatorOutput.time', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gvw_est', full_name='com.michelin.bib.embedded.GVWEstimatorOutput.gvw_est', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sigma', full_name='com.michelin.bib.embedded.GVWEstimatorOutput.sigma', index=2,
      number=3, type=2, cpp_type=6, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1038,
  serialized_end=1104,
)


_ECODRIVINGESTIMATOROUTPUT = _descriptor.Descriptor(
  name='EcoDrivingEstimatorOutput',
  full_name='com.michelin.bib.embedded.EcoDrivingEstimatorOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='t_ini', full_name='com.michelin.bib.embedded.EcoDrivingEstimatorOutput.t_ini', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='t_end', full_name='com.michelin.bib.embedded.EcoDrivingEstimatorOutput.t_end', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='com.michelin.bib.embedded.EcoDrivingEstimatorOutput.type', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ECODRIVINGESTIMATOROUTPUT_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1107,
  serialized_end=1319,
)


_ENERGETICDIAGNOSISOUTPUT = _descriptor.Descriptor(
  name='EnergeticDiagnosisOutput',
  full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.time', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fuelConsumptionL', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.fuelConsumptionL', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indicatedEnergykWh', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.indicatedEnergykWh', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frictionEnergykWh', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.frictionEnergykWh', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='effectiveEnergykWh', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.effectiveEnergykWh', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distanceTransGearKm', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.distanceTransGearKm', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='durationClutchStateS', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.durationClutchStateS', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='durationTransGearS', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.durationTransGearS', index=7,
      number=8, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distancePowertrainStateKm', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.distancePowertrainStateKm', index=8,
      number=9, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='durationPowertrainStateS', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.durationPowertrainStateS', index=9,
      number=10, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distanceClutchStateKm', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.distanceClutchStateKm', index=10,
      number=11, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auxiliariesEnergykWh', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.auxiliariesEnergykWh', index=11,
      number=12, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='powerTakeOffEnergykWh', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.powerTakeOffEnergykWh', index=12,
      number=13, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primaryEnergykWh', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.primaryEnergykWh', index=13,
      number=14, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wheelEnergykWh', full_name='com.michelin.bib.embedded.EnergeticDiagnosisOutput.wheelEnergykWh', index=14,
      number=15, type=1, cpp_type=5, label=3,
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
  serialized_start=1322,
  serialized_end=1769,
)

_VSPOUTPUTDATA.fields_by_name['availableSignals'].enum_type = _VSPOUTPUTDATA_SIGNAL
_VSPOUTPUTDATA_SIGNAL.containing_type = _VSPOUTPUTDATA
_ECODRIVINGESTIMATOROUTPUT.fields_by_name['type'].enum_type = _ECODRIVINGESTIMATOROUTPUT_TYPE
_ECODRIVINGESTIMATOROUTPUT_TYPE.containing_type = _ECODRIVINGESTIMATOROUTPUT
DESCRIPTOR.message_types_by_name['VSPOutputData'] = _VSPOUTPUTDATA
DESCRIPTOR.message_types_by_name['VSPOutputSignals'] = _VSPOUTPUTSIGNALS
DESCRIPTOR.message_types_by_name['GVWEstimatorOutput'] = _GVWESTIMATOROUTPUT
DESCRIPTOR.message_types_by_name['EcoDrivingEstimatorOutput'] = _ECODRIVINGESTIMATOROUTPUT
DESCRIPTOR.message_types_by_name['EnergeticDiagnosisOutput'] = _ENERGETICDIAGNOSISOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VSPOutputData = _reflection.GeneratedProtocolMessageType('VSPOutputData', (_message.Message,), {
  'DESCRIPTOR' : _VSPOUTPUTDATA,
  '__module__' : 'Embedded_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.embedded.VSPOutputData)
  })
_sym_db.RegisterMessage(VSPOutputData)

VSPOutputSignals = _reflection.GeneratedProtocolMessageType('VSPOutputSignals', (_message.Message,), {
  'DESCRIPTOR' : _VSPOUTPUTSIGNALS,
  '__module__' : 'Embedded_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.embedded.VSPOutputSignals)
  })
_sym_db.RegisterMessage(VSPOutputSignals)

GVWEstimatorOutput = _reflection.GeneratedProtocolMessageType('GVWEstimatorOutput', (_message.Message,), {
  'DESCRIPTOR' : _GVWESTIMATOROUTPUT,
  '__module__' : 'Embedded_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.embedded.GVWEstimatorOutput)
  })
_sym_db.RegisterMessage(GVWEstimatorOutput)

EcoDrivingEstimatorOutput = _reflection.GeneratedProtocolMessageType('EcoDrivingEstimatorOutput', (_message.Message,), {
  'DESCRIPTOR' : _ECODRIVINGESTIMATOROUTPUT,
  '__module__' : 'Embedded_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.embedded.EcoDrivingEstimatorOutput)
  })
_sym_db.RegisterMessage(EcoDrivingEstimatorOutput)

EnergeticDiagnosisOutput = _reflection.GeneratedProtocolMessageType('EnergeticDiagnosisOutput', (_message.Message,), {
  'DESCRIPTOR' : _ENERGETICDIAGNOSISOUTPUT,
  '__module__' : 'Embedded_pb2'
  # @@protoc_insertion_point(class_scope:com.michelin.bib.embedded.EnergeticDiagnosisOutput)
  })
_sym_db.RegisterMessage(EnergeticDiagnosisOutput)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)