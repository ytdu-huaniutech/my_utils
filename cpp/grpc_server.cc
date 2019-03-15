#include <iostream>
#include <unistd.h>

#include <grpc++/grpc++.h>
#include "proto/hello.grpc.pb.h"
#include "proto/hello.pb.h"

class HelloImpl final : public hello::Hello::Service{
  ::grpc::Status Hello(::grpc::ServerContext* context,
                       const ::hello::HelloInput* request,
                       ::hello::HelloOutput* response) override {
    std::cout << "hello to " << request->name() << std::endl;
    std::string message = "";
    for (int i = 0; i < request->repeat(); ++i) {
      message += "Hello! ";
    }
    message += request->name();
    response->set_hello_message(message);
    return ::grpc::Status::OK;
  }
};

void sigHandler(int signum) {
  std::cerr << "Terminating! Wait " << 10 << " seconds to finish processing...\n";
  sleep(10);
  std::cerr << "Terminated!";
  exit(signum);
}

int main() {
  std::string server_address = "[::]:9988";
  HelloImpl hello;

  ::grpc::ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&hello);
  
  std::unique_ptr<::grpc::Server> server(builder.BuildAndStart());
  std::cout << "Server listening on " << server_address << std::endl;

  if (signal(SIGTERM, sigHandler) == SIG_ERR
    || signal(SIGINT, sigHandler) == SIG_ERR) {
    std::cerr << "handle signal failed";
    exit(1);
  }

  server->Wait();
}
