# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/process.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proto/process.proto\x12\x05proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xba\x01\n\nProcStatus\x12\x0e\n\x06status\x18\x01 \x01(\t\x12.\n\nstarted_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x06uptime\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x10\n\x08restarts\x18\x04 \x01(\x05\x12\x0b\n\x03\x63pu\x18\x05 \x01(\t\x12\x0e\n\x06memory\x18\x06 \x01(\t\x12\x12\n\nparent_pid\x18\x07 \x01(\x05\"\xa4\x02\n\x07Process\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x0f\n\x07scripts\x18\x04 \x03(\t\x12\x17\n\x0f\x65xecutable_path\x18\x05 \x01(\t\x12\x0b\n\x03pid\x18\x06 \x01(\x05\x12\x14\n\x0c\x61uto_restart\x18\x07 \x01(\x08\x12\x0b\n\x03\x63wd\x18\x08 \x01(\t\x12\x15\n\rpid_file_path\x18\t \x01(\t\x12\x15\n\rlog_file_path\x18\n \x01(\t\x12\x15\n\rerr_file_path\x18\x0b \x01(\t\x12\x17\n\x0f\x63ron_expression\x18\x0c \x01(\t\x12&\n\x0bproc_status\x18\x0e \x01(\x0b\x32\x11.proto.ProcStatus\x12\x11\n\tstop_next\x18\x0f \x01(\x08\"\xe7\x01\n\x11\x41\x64\x64ProcessRequest\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x0f\n\x07scripts\x18\x04 \x03(\t\x12\x17\n\x0f\x65xecutable_path\x18\x05 \x01(\t\x12\x0b\n\x03pid\x18\x06 \x01(\x05\x12\x14\n\x0c\x61uto_restart\x18\x07 \x01(\x08\x12\x0b\n\x03\x63wd\x18\x08 \x01(\t\x12\x15\n\rpid_file_path\x18\t \x01(\t\x12\x15\n\rlog_file_path\x18\n \x01(\t\x12\x15\n\rerr_file_path\x18\x0b \x01(\t\x12\x17\n\x0f\x63ron_expression\x18\x0c \x01(\t\"\"\n\x12\x46indProcessRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\".\n\x12StopProcessRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\"&\n\x13StopProcessResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\xf5\x01\n\x13StartProcessRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x03(\t\x12\x0f\n\x07scripts\x18\x04 \x03(\t\x12\x17\n\x0f\x65xecutable_path\x18\x05 \x01(\t\x12\x0b\n\x03pid\x18\x06 \x01(\x05\x12\x14\n\x0c\x61uto_restart\x18\x07 \x01(\x08\x12\x0b\n\x03\x63wd\x18\x08 \x01(\t\x12\x15\n\rpid_file_path\x18\t \x01(\t\x12\x15\n\rlog_file_path\x18\n \x01(\t\x12\x15\n\rerr_file_path\x18\x0b \x01(\t\x12\x17\n\x0f\x63ron_expression\x18\x0c \x01(\t\"\x14\n\x12ListProcessRequest\"8\n\x13ListProcessResponse\x12!\n\tprocesses\x18\x01 \x03(\x0b\x32\x0e.proto.Process\"\"\n\x14\x44\x65leteProcessRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"(\n\x15\x44\x65leteProcessResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x97\x01\n\x13SpawnProcessRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\x12\x0f\n\x07scripts\x18\x03 \x03(\t\x12\x17\n\x0f\x65xecutable_path\x18\x04 \x01(\t\x12\x14\n\x0c\x61uto_restart\x18\x06 \x01(\x08\x12\x0b\n\x03\x63wd\x18\x07 \x01(\t\x12\x17\n\x0f\x63ron_expression\x18\x0b \x01(\t\"\'\n\x14SpawnProcessResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xed\x03\n\x0eProcessManager\x12\x38\n\nAddProcess\x12\x18.proto.AddProcessRequest\x1a\x0e.proto.Process\"\x00\x12<\n\x0cStartProcess\x12\x1a.proto.StartProcessRequest\x1a\x0e.proto.Process\"\x00\x12\x46\n\x0bStopProcess\x12\x19.proto.StopProcessRequest\x1a\x1a.proto.StopProcessResponse\"\x00\x12:\n\x0b\x46indProcess\x12\x19.proto.FindProcessRequest\x1a\x0e.proto.Process\"\x00\x12L\n\rDeleteProcess\x12\x1b.proto.DeleteProcessRequest\x1a\x1c.proto.DeleteProcessResponse\"\x00\x12\x46\n\x0bListProcess\x12\x19.proto.ListProcessRequest\x1a\x1a.proto.ListProcessResponse\"\x00\x12I\n\x0cSpawnProcess\x12\x1a.proto.SpawnProcessRequest\x1a\x1b.proto.SpawnProcessResponse\"\x00\x42\x03Z\x01.b\x06proto3')



_PROCSTATUS = DESCRIPTOR.message_types_by_name['ProcStatus']
_PROCESS = DESCRIPTOR.message_types_by_name['Process']
_ADDPROCESSREQUEST = DESCRIPTOR.message_types_by_name['AddProcessRequest']
_FINDPROCESSREQUEST = DESCRIPTOR.message_types_by_name['FindProcessRequest']
_STOPPROCESSREQUEST = DESCRIPTOR.message_types_by_name['StopProcessRequest']
_STOPPROCESSRESPONSE = DESCRIPTOR.message_types_by_name['StopProcessResponse']
_STARTPROCESSREQUEST = DESCRIPTOR.message_types_by_name['StartProcessRequest']
_LISTPROCESSREQUEST = DESCRIPTOR.message_types_by_name['ListProcessRequest']
_LISTPROCESSRESPONSE = DESCRIPTOR.message_types_by_name['ListProcessResponse']
_DELETEPROCESSREQUEST = DESCRIPTOR.message_types_by_name['DeleteProcessRequest']
_DELETEPROCESSRESPONSE = DESCRIPTOR.message_types_by_name['DeleteProcessResponse']
_SPAWNPROCESSREQUEST = DESCRIPTOR.message_types_by_name['SpawnProcessRequest']
_SPAWNPROCESSRESPONSE = DESCRIPTOR.message_types_by_name['SpawnProcessResponse']
ProcStatus = _reflection.GeneratedProtocolMessageType('ProcStatus', (_message.Message,), {
  'DESCRIPTOR' : _PROCSTATUS,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.ProcStatus)
  })
_sym_db.RegisterMessage(ProcStatus)

Process = _reflection.GeneratedProtocolMessageType('Process', (_message.Message,), {
  'DESCRIPTOR' : _PROCESS,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.Process)
  })
_sym_db.RegisterMessage(Process)

AddProcessRequest = _reflection.GeneratedProtocolMessageType('AddProcessRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDPROCESSREQUEST,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.AddProcessRequest)
  })
_sym_db.RegisterMessage(AddProcessRequest)

FindProcessRequest = _reflection.GeneratedProtocolMessageType('FindProcessRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDPROCESSREQUEST,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.FindProcessRequest)
  })
_sym_db.RegisterMessage(FindProcessRequest)

StopProcessRequest = _reflection.GeneratedProtocolMessageType('StopProcessRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPPROCESSREQUEST,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.StopProcessRequest)
  })
_sym_db.RegisterMessage(StopProcessRequest)

StopProcessResponse = _reflection.GeneratedProtocolMessageType('StopProcessResponse', (_message.Message,), {
  'DESCRIPTOR' : _STOPPROCESSRESPONSE,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.StopProcessResponse)
  })
_sym_db.RegisterMessage(StopProcessResponse)

StartProcessRequest = _reflection.GeneratedProtocolMessageType('StartProcessRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTPROCESSREQUEST,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.StartProcessRequest)
  })
_sym_db.RegisterMessage(StartProcessRequest)

ListProcessRequest = _reflection.GeneratedProtocolMessageType('ListProcessRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROCESSREQUEST,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.ListProcessRequest)
  })
_sym_db.RegisterMessage(ListProcessRequest)

ListProcessResponse = _reflection.GeneratedProtocolMessageType('ListProcessResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROCESSRESPONSE,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.ListProcessResponse)
  })
_sym_db.RegisterMessage(ListProcessResponse)

DeleteProcessRequest = _reflection.GeneratedProtocolMessageType('DeleteProcessRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPROCESSREQUEST,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.DeleteProcessRequest)
  })
_sym_db.RegisterMessage(DeleteProcessRequest)

DeleteProcessResponse = _reflection.GeneratedProtocolMessageType('DeleteProcessResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPROCESSRESPONSE,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.DeleteProcessResponse)
  })
_sym_db.RegisterMessage(DeleteProcessResponse)

SpawnProcessRequest = _reflection.GeneratedProtocolMessageType('SpawnProcessRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPAWNPROCESSREQUEST,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.SpawnProcessRequest)
  })
_sym_db.RegisterMessage(SpawnProcessRequest)

SpawnProcessResponse = _reflection.GeneratedProtocolMessageType('SpawnProcessResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPAWNPROCESSRESPONSE,
  '__module__' : 'proto.process_pb2'
  # @@protoc_insertion_point(class_scope:proto.SpawnProcessResponse)
  })
_sym_db.RegisterMessage(SpawnProcessResponse)

_PROCESSMANAGER = DESCRIPTOR.services_by_name['ProcessManager']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\001.'
  _PROCSTATUS._serialized_start=96
  _PROCSTATUS._serialized_end=282
  _PROCESS._serialized_start=285
  _PROCESS._serialized_end=577
  _ADDPROCESSREQUEST._serialized_start=580
  _ADDPROCESSREQUEST._serialized_end=811
  _FINDPROCESSREQUEST._serialized_start=813
  _FINDPROCESSREQUEST._serialized_end=847
  _STOPPROCESSREQUEST._serialized_start=849
  _STOPPROCESSREQUEST._serialized_end=895
  _STOPPROCESSRESPONSE._serialized_start=897
  _STOPPROCESSRESPONSE._serialized_end=935
  _STARTPROCESSREQUEST._serialized_start=938
  _STARTPROCESSREQUEST._serialized_end=1183
  _LISTPROCESSREQUEST._serialized_start=1185
  _LISTPROCESSREQUEST._serialized_end=1205
  _LISTPROCESSRESPONSE._serialized_start=1207
  _LISTPROCESSRESPONSE._serialized_end=1263
  _DELETEPROCESSREQUEST._serialized_start=1265
  _DELETEPROCESSREQUEST._serialized_end=1299
  _DELETEPROCESSRESPONSE._serialized_start=1301
  _DELETEPROCESSRESPONSE._serialized_end=1341
  _SPAWNPROCESSREQUEST._serialized_start=1344
  _SPAWNPROCESSREQUEST._serialized_end=1495
  _SPAWNPROCESSRESPONSE._serialized_start=1497
  _SPAWNPROCESSRESPONSE._serialized_end=1536
  _PROCESSMANAGER._serialized_start=1539
  _PROCESSMANAGER._serialized_end=2032
# @@protoc_insertion_point(module_scope)
