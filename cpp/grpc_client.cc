#include <iostream>
#include <grpc++/grpc++.h>
#include "proto/hello.grpc.pb.h"
#include "proto/hello.pb.h"


int main() {
  auto channel = grpc::CreateChannel("localhost:9988", grpc::InsecureChannelCredentials());
  auto stub = hello::Hello::NewStub(channel);
  grpc::ClientContext context;
  auto request = hello::HelloInput();
  request.set_name("ytdu");
  request.set_repeat(3);
  auto result = hello::HelloOutput();
  stub->Hello(&context, request, &result);
  std::cout << result.hello_message() << std::endl;
  return 0;
}
