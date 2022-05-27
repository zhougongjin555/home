package main

import (
	"bufio"
	pb "client/proto"
	"context"
	"fmt"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/metadata"
	"io"
	"log"
	"os"
	"strings"
	"time"
)

func streamInterceptor(ctx context.Context, desc *grpc.StreamDesc, cc *grpc.ClientConn, method string, streamer grpc.Streamer, opts ...grpc.CallOption) (grpc.ClientStream, error) {
	return nil, nil
}

func AiGrpcTrans(c pb.AiRepliesClient) error {
	// metadata 测试
	md := metadata.Pairs("timestamp", time.Now().Format("2006-01-02 15:04:05")) // 注意时间戳格式
	ctx := metadata.NewOutgoingContext(context.Background(), md)                // 新建通道，并包装数据

	//ctx, cancel := context.WithCancel(context.Background())
	//defer cancel()
	// 监听服务端对应服务的的流式响应
	stream, err := c.Reply(ctx) // reply为我们自己定义的服务
	if err != nil {
		log.Fatalf("AiService client get response error: %v", err)
		return err
	}

	// 此步定义一个值可以为任意类型的通道，并利用通道未关闭并取值无值可取时会阻塞的特定，对主函数进行阻塞，防止goroutine提前退出
	waitchan := make(chan struct{})

	// 使用goroutine对服务放回的数据携程进行处理  +  闭包
	go func() {
		// goroutine 执行结束向通道塞一个数据
		defer func() {
			waitchan <- struct{}{}
		}()

		// 从流式响应对象中取出数据打印
		for {
			in, err := stream.Recv()
			if err == io.EOF {
				// 数据已经全部取出
				close(waitchan) // 直接关闭通道
				return
			}
			if err != nil {
				log.Fatalf("AiService Client get data from stream error: %v", err)
				return
			}
			fmt.Printf("AI: %s\n", in.GetReply()) // 使用了proto定义的取值方法，隐式调用
		}
	}()

	// goroutine不断从终端获取输入
	go func() {
		// 1, 从终端获取输入信息
		// 2, 向rpc服务发送数据，并接受返回
		reader := bufio.NewReader(os.Stdin)
		var id int64 = 0

		// 从metadata中拿数据
		header, err := stream.Header()
		if err != nil {
			log.Fatalf("AiService client get metadata fail: %v", err)
		}
		if t, ok := header["token"]; ok {
			fmt.Println("AiService client get metadata header['token'] success! ")
			for i, v := range t {
				fmt.Printf("header['token'], index: %d, value: %s\n", i, v)
			}
		} else {
			log.Fatalln("AiService client get metadata header['token'] failed! ")
		}

		for {
			c, _ := reader.ReadString('\n')
			c = strings.TrimSpace(c) // 必须要去除空格，不然安全词无法跳出
			if len(c) == 0 {
				continue
			}
			if strings.ToUpper(c) == "Q" {
				log.Println("对话终止...")
				break
			}
			_ = stream.Send(&pb.Inputs{Id: id, Input: c})
			id++
		}
		err = stream.CloseSend()
		if err != nil {
			return
		} // 关闭发送流
	}()

	<-waitchan // 阻塞主进程
	return nil
}

func AiGrpcClient() {
	// 要求连接携带证书，并创建第一个初始的空证书
	conn, err := grpc.Dial("127.0.0.1:9999", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("AiService CLient Conn Fail: %v", err)
	}
	defer conn.Close()

	// 新建一个客户端
	c := pb.NewAiRepliesClient(conn)

	// 执行grpc调用
	log.Println("请开始与AI的对话...")
	err = AiGrpcTrans(c)
	if err != nil {
		log.Fatalf("AiService client trans rpc error: %v", err)
	}
}
