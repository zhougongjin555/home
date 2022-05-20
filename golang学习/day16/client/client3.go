// 基于json传输协议的rpc
package main

import (
	"fmt"
	"log"
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"
)

func ClientDemo3() {
	// 建立TCP连接
	conn, err := net.Dial("tcp", "127.0.0.1:9999")
	if err != nil {
		log.Fatal("dialing:", err)
	}
	// 使用JSON协议
	client := rpc.NewClientWithCodec(jsonrpc.NewClientCodec(conn))
	// 同步调用
	args := &Args{12, 16}
	var reply int
	err = client.Call("ServiceA.Square", args, &reply)
	if err != nil {
		log.Fatal("ServiceA.Square error:", err)
	}
	fmt.Println("ServiceA.Square:", reply)

	// 异步调用
	var reply2 int
	divCall := client.Go("ServiceA.Square", args, &reply2, nil)
	replyCall := <-divCall.Done // 接收调用结果
	fmt.Println(replyCall.Error)
	fmt.Println(reply2)
}
