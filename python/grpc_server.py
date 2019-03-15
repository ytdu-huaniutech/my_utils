import signal
import time
from concurrent import futures

import grpc

from proto.hello_pb2 import HelloInput, HelloOutput
from proto.hello_pb2_grpc import HelloServicer, add_HelloServicer_to_server


class HelloServicerImpl(HelloServicer):
    def __init__(self):
        super().__init__()

    def Hello(self, request, context):
        print('hello to', request.name)
        message = 'Hello! ' * request.repeat + request.name
        return HelloOutput(hello_message=message)


def sigterm_handler(signal, frame):
    global IS_ALL_READY
    _logger.warn("SIGTERM received, server is closing after 10 secs")
    IS_ALL_READY = False
    time.sleep(10)
    _logger.warn("server closed")
    import sys
    sys.exit(0)


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_servicer = HelloServicerImpl()
    add_HelloServicer_to_server(hello_servicer, server)
    server.add_insecure_port('[::]:9988')
    server.start()
    print('Listening at port 9988')
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    signal.signal(signal.SIGTERM, sigterm_handler)
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
