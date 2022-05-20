package main

import (
	"context"
	pb "day16/address"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
	"net"
	"time"
)

type birthyearserver struct {
	pb.UnimplementedBirthYearServiceServer
}

type aftertwoyearageserver struct {
	pb.UnimplementedTwoAfterYearAgeServiceServer
}

func (t *testserver) BirthYear(ctx context.Context, in *pb.StudentRequest) (*pb.StudentResponse, error) {
	tyear := time.Now().Year()
	age := in.Age
	byear := int32(tyear) - age
	var sr []*pb.StudentRequest
	sr = append(sr, in)
	return &pb.StudentResponse{StudentRequestFields: sr, Year: byear}, nil
}

func (t *testserver) TwoAfterYearAge(ctx context.Context, in *pb.StudentRequest) (*pb.StudentResponse, error) {
	year := time.Now().Year()
	var sr []*pb.StudentRequest
	sr = append(sr, in)
	return &pb.StudentResponse{StudentRequestFields: sr, Year: int32(year) + 2}, nil
}

func MytestGrpcDemo() {
	// 监听本地的端口
	lis, err := net.Listen("tcp", ":9999")
	if err != nil {
		panic(err)
	}

	// 创建grpc服务器
	s := grpc.NewServer()
	// 为grpc服务器注册服务！！！！
	pb.RegisterBirthYearServiceServer(s, &birthyearserver{})
	pb.RegisterTwoAfterYearAgeServiceServer(s, &aftertwoyearageserver{})

	// 为grpc服务器注册反射服务
	reflection.Register(s)
	// Serve方法在lis上接受传入连接，为每个连接创建一个ServerTransport和server的goroutine。
	// 该goroutine读取gRPC请求，然后调用已注册的处理程序来响应它们。
	err = s.Serve(lis)
	if err != nil {
		panic(err)
	}
}
