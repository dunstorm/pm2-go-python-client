import logging
from typing import List

import grpc
import proto.process_pb2 as process_pb2
import proto.process_pb2_grpc as process_pb2_grpc

class Duration(object):
    seconds: int

class Timestamp(Duration):
    nanos: int

class ProcStatus(object):
    status: str
    started_at: Timestamp
    uptime: Duration
    restarts: int
    cpu: str
    memory: str

class Process(object):
    id: int
    name: str
    executable_path: str
    pid: int = 0
    auto_restart: bool = False
    cwd: str = ""
    cron_expression: str = ""
    args: List[str] = []
    scripts: List[str] = []

    pid_file_path: str
    log_file_path: str
    err_file_path: str

    proc_status: ProcStatus


class ProcessClient(object):

    def __init__(self, host: str = "localhost", port: int = 9001) -> None:
        self.channel = grpc.insecure_channel('{}:{}'.format(host, port))
        self.stub = process_pb2_grpc.ProcessManagerStub(self.channel)

    def add_process(self, process: Process) -> Process:
        request = process_pb2.AddProcessRequest()
        request.name = process.name
        request.executable_path = process.executable_path
        request.pid = process.pid
        request.auto_restart = process.auto_restart
        request.cwd = process.cwd
        request.pid_file_path = process.pid_file_path
        request.log_file_path = process.log_file_path
        request.err_file_path = process.err_file_path
        request.cron_expression = process.cron_expression
        request.args = process.args
        request.scripts = process.scripts
        
        response = self.stub.AddProcess(request)
        return response

    def spawn_process(self, process: Process) -> bool:
        request = process_pb2.SpawnProcessRequest()
        request.name = process.name
        request.executable_path = process.executable_path
        request.auto_restart = process.auto_restart
        request.cwd = process.cwd
        request.cron_expression = process.cron_expression
        request.args.extend(process.args)
        request.scripts.extend(process.scripts)
        
        response = self.stub.SpawnProcess(request)
        return response

    def list_processes(self) -> List[Process]:
        request = process_pb2.ListProcessRequest()
        response = self.stub.ListProcess(request)
        return response.processes

if __name__ == '__main__':
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    client = ProcessClient()

    # new_process = Process()
    # new_process.name = "test"
    # new_process.executable_path = "celery"
    # new_process.args = ["worker"]
    # new_process.scripts = ["logs_date"]

    # success = client.spawn_process(new_process)
    # if not success:
    #     logger.error("Failed to spawn process")
    #     exit(1)

    processes = client.list_processes()

    if len(processes) < 1:
        logger.info("No processes found")
    
    for process in processes:
        logger.info(process.name)