pip install grpcio
pip install grpcio-tools
pip install protobuf

cd ..
python -m grpc_tools.protoc --python_out=. -I. --grpc_python_out=. proto/*.proto
protoc -I. --cpp_out=. proto/*.proto
protoc -I. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` proto/*.proto
