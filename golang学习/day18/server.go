package main

import (
	"context"
	pb "day18/pb"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/health"
	"google.golang.org/grpc/health/grpc_health_v1"
	"google.golang.org/grpc/metadata"
	"google.golang.org/grpc/status"
	"log"
	"net"
	"os"
	"os/signal"
	"strconv"
	"strings"
	"syscall"
)

var (
	errMetadata     = status.Errorf(codes.InvalidArgument, "missing metadata!")
	errInvalidToken = status.Errorf(codes.Unauthenticated, "Invalid token")
)

type ShopService struct {
	pb.UnimplementedGetPriceServiceServer
}

// 带有metadata的服务
func (s *ShopService) GetPrice(ctx context.Context, in *pb.Req) (*pb.Res, error) {
	// 正常业务逻辑
	fruit := strings.ToLower(in.Fruit.String())
	fmt.Println("fruit", in.Fruit, fruit)
	res := GetParamFromApollo(fruit, "")
	price, _ := strconv.Atoi(res)
	fmt.Printf("return %s's price == %d", fruit, price)
	return &pb.Res{Fruit: in.Fruit, Price: int64(price)}, nil
}

func Valid(auth []string) bool {
	if len(auth) < 1 {
		return false
	}
	token := strings.TrimSpace(auth[0])
	return token == "zhougongjin"
}

// 一元拦截器
func unaryInterceptor(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {
	/* 针对metadata相关
	1, 尝试接收从客户端传入的metadata数据2
	2, 手动赋予metadata header&trailer 数据，注意不同数据类型赋值方法不一致
	3, grpc.set___()
	*/
	md, ok := metadata.FromIncomingContext(ctx) // 从客户端传入的metadata中获取数据
	if !ok {
		return nil, errMetadata
	}
	if !Valid(md["auth"]) {
		return nil, errInvalidToken
	}

	// 设置返回的header && trailer
	//defer func() {
	//	trailer := metadata.Pairs("")
	//	grpc.SetTrailer(ctx, trailer)
	//}()
	//header := metadata.New(map[string]string{"auth": md["auth"][0], "passkey": md["auth"][0] + "security"})
	//grpc.SetHeader(ctx, header)

	// 返回处理器函数
	m, err := handler(ctx, req)
	if err != nil {
		log.Fatalf("server interceptor return error: %s", err)
	}
	return m, nil
}

func server() {
	/*
		1, 监听端口： 接收处理服务端请求
		2, 创建grpc服务器
		3, 再grpc服务器上注册自己的服务
		4, 连接consul
		5, (异步) 启动grpc服务，s.Server(lis)
		6, (异步) 将服务注册到consul
	*/

	port := GetParamFromApollo("port", "")

	// 监听客户端
	listen, err := net.Listen("tcp", ":"+port)
	if err != nil {
		log.Fatalf("server init listen error: %s", err)
	}

	// 新建grpc服务器，并注册服务
	s := grpc.NewServer(grpc.UnaryInterceptor(unaryInterceptor)) // 创建服务同时添加中间件函数
	pb.RegisterGetPriceServiceServer(s, &ShopService{})

	// 为grpc服务器注册一个健康检查
	healthcheck := health.NewServer()
	grpc_health_v1.RegisterHealthServer(s, healthcheck)

	// 启动服务(防止启动服务出错或者注册服务出错导致程序崩溃)
	go func() {
		err = s.Serve(listen)
		if err != nil {
			log.Fatalf("server start error: %s", err)
		}
	}()

	// 初始化并注册consul
	serviceID := "get_fruit_price_service_20220613"
	c, err := NewConsul("127.0.0.1:8500") // 初始化ip为consul web端地址
	if err != nil {
		log.Fatalf("server init consul error: %s", err)
	}
	err = c.RegisterService(serviceID, "localhost")
	if err != nil {
		return
	} // 服务注册ip为本地服务的ip地址

	// 实现程序退出后自动在consul注销服务
	quitChan := make(chan os.Signal)
	signal.Notify(quitChan, syscall.SIGTERM, syscall.SIGINT, syscall.SIGKILL) // ctrl+c退出，kill -9退出都会发类似的信号
	<-quitChan                                                                // 阻塞函数直到有退出信号
	c.DeregisterService(serviceID)
}
