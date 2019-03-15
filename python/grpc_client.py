import grpc

from proto.hello_pb2 import HelloInput, HelloOutput
from proto.hello_pb2_grpc import HelloStub


if __name__ == '__main__':
    with grpc.insecure_channel('localhost:9988') as channel:
        stub = HelloStub(channel)
        request = HelloInput(name='ytdu', repeat=3)
        response = stub.Hello(request, None)
        print(response.hello_message)
