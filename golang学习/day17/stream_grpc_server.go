package main

import (
	pb "day17/proto"
	"fmt"
	"github.com/hashicorp/consul/api"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/metadata"
	"google.golang.org/grpc/status"
	"log"
	"net"
	"strings"
	"time"
)

type AiServer struct {
	pb.UnimplementedAiRepliesServer
}

func (a *AiServer) Reply(stream pb.AiReplies_ReplyServer) error {

	// 设置trailer数据
	defer func() {
		trailer := metadata.Pairs("timestamp", time.Now().Format("2006/01/02---15:04:05"))
		stream.SetTrailer(trailer)
	}()

	// 从metadata中获取client发送的数据
	md, ok := metadata.FromIncomingContext(stream.Context())
	if !ok {
		return status.Errorf(codes.DataLoss, "AiService server get metadata from client fail!")
	}

	if t, ok := md["timestamp"]; ok {
		fmt.Println("timestamp data from metadata:")
		for i, v := range t {
			fmt.Printf("index: %d, value: %s", i, v)
		}
	}

	// 创建和发送metadata header数据
	header := metadata.Pairs("token", "123456789")
	err := stream.SendHeader(header)
	if err != nil {
		return err
	}

	for {
		in, err := stream.Recv()
		if err != nil {
			log.Fatalf("AiService Server Recv data error: %v", err)
			//return err
		}
		reply := Magic(in.Input)

		// 流式返回响应信息
		if err = stream.Send(&pb.Replies{Reply: reply}); err != nil {
			log.Fatalf("AiService server send reply data error: %v", err)
		}
	}
}

// 将本地服务注册到consul
func RegisterService() error {
	client, err := api.NewClient(api.DefaultConfig())
	if err != nil {
		log.Fatalf("Aiservice server create newclient error: %v", err)
	}

	srv := &api.AgentServiceRegistration{
		ID:      "AiService-2022-05-06",
		Name:    "AiService",
		Tags:    []string{"周公瑾", "诸葛亮"},
		Address: "127.0.0.1",
		Port:    9999,
	}
	return client.Agent().ServiceRegister(srv)
}

func Magic(s string) string {
	s = strings.TrimSpace(s) // 去除两边空格
	s = strings.ReplaceAll(s, "吗", "")
	s = strings.ReplaceAll(s, "吧", "")
	s = strings.ReplaceAll(s, "啊", "")
	s = strings.ReplaceAll(s, "？", "！")
	s = strings.ReplaceAll(s, "你", "我")
	s = strings.ReplaceAll(s, "?", "!")
	return s
}

func AiGrpcDemo() {
	// 1, 监听端口
	lis, err := net.Listen("tcp", ":9999")
	if err != nil {
		log.Fatalf("Apiservice server listen start fail: %v", err)
	}

	// 2, 新建服务器并注册服务
	s := grpc.NewServer()                      // 新建grpc服务器
	pb.RegisterAiRepliesServer(s, &AiServer{}) // 注册服务到服务器

	// 2.5 将服务同步注册到consul
	if err = RegisterService(); err != nil {
		log.Fatalf("AiService server register error: %v", err)
	}

	// 3, 启动服务器
	err = s.Serve(lis)
	if err != nil {
		log.Fatalf("ApiService server start fail: %v", err)
	}
}
