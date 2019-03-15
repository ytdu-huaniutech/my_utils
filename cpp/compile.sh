cd ..
g++ -o cpp/grpc_client --std=c++11 -lgrpc++ -lprotobuf cpp/grpc_client.cc proto/*.cc
g++ -o cpp/grpc_server --std=c++11 -lgrpc++ -lprotobuf cpp/grpc_server.cc proto/*.cc
