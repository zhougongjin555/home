package main

import (
	"context"
	pb "day16/address"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
	"log"
	"net"
)

type server struct{}

func (s *server) SayHello(ctx context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
	return &pb.HelloReply{Message: "Hello " + in.Name}, nil
}

func GRpcDemo() {
	lis, err := net.Listen("tcp", ":8003")
	if err != nil {
		log.Fatal(err)
		return
	}
	s := grpc.NewServer()                  // 新建grpc服务器
	pb.RegisterGreeterServer(s, &server{}) // 在gRPC服务端注册服务

	reflection.Register(s)
	err = s.Serve(lis)
	if err != nil {
		log.Fatal(err)
		return
	}

}
