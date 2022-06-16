package main

import (
	"bufio"
	pb "client/pb"
	"context"
	"fmt"
	"github.com/shima-park/agollo"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/metadata"
	"log"
	"os"
	"strings"
)

func GetParamFromApollo(key string) (val string) {
	a, err := agollo.New(
		"localhost:8080",
		"PriceService",
		agollo.DefaultNamespace("application"),
		agollo.AutoFetchOnCacheMiss(),
		agollo.Cluster("default"),
	)
	if err != nil {
		return
	}
	val = a.Get(key, agollo.WithDefault("UnKnown"))
	return val
}

func Input() (name pb.Fruit, err error) {
EDGE:
	for {
		rd := bufio.NewReader(os.Stdin)
		fmt.Printf("Enter the fruit you interest: ")
		fruit, _ := rd.ReadString('\n')
		fruit = strings.TrimSpace(fruit)
		fruit = strings.ToLower(fruit)

		switch fruit {
		case "apple":
			name = pb.Fruit_APPLE
			break EDGE
		case "orange":
			name = pb.Fruit_ORANGE
			break EDGE
		case "banana":
			name = pb.Fruit_BANANA
			break EDGE
		case "watermelon":
			name = pb.Fruit_WATERMELON
			break EDGE
		default:
			fmt.Println("we dont have this fruit price!")
		}
	}
	return name, nil
}

func Client() {
	port := GetParamFromApollo("port")
	conn, err := grpc.Dial("127.0.0.1:"+port, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("client init error: %s", err)
	}
	defer conn.Close()

	// 新建grpc客户端
	c := pb.NewGetPriceServiceClient(conn)
	/* 携带metadata进行服务端验证
	1, 设置client --> server metadata数据
	2, metadata.NewOutgoingContext 发送数据
	3, 设置变量header, trailer 用来传送给服务端、并接收服务端放入的数据
	4, 将变量放入请求服务之中，并后续处理操作
	*/
	auth := GetParamFromApollo("auth")
	md := metadata.Pairs("auth", auth)
	ctx := metadata.NewOutgoingContext(context.Background(), md)
	var header, trailer metadata.MD
	//ctx, cancel := context.WithCancel(context.Background())
	//defer cancel()

	name, _ := Input()

	res, err := c.GetPrice(ctx, &pb.Req{Fruit: name}, grpc.Header(&header), grpc.Trailer(&trailer)) // 请求的时候要携带结构体
	if err != nil {
		log.Fatalf("client get response from server error: %s", err)
	}
	fmt.Printf("This fruit(%s) price == %d", res.GetFruit(), res.GetPrice())

	// ... 用来接收服务端返回的metadata数据进行一些操作，暂时不演示了
}
