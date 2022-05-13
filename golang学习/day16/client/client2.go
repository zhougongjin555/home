// 基于go内部库实现rpc服务
package main

import (
	"fmt"
	"log"
	"net/rpc"
)

// 定义微服务接受的全部参数
type Args struct {
	X, Y float64
}

func ClientDemo2() {
	// 基于http的客户端
	//client, err := rpc.DialHTTP("tcp", "127.0.0.1:9999")

	// 基于tcp的客户端
	client, err := rpc.Dial("tcp", "127.0.0.1:9999")
	if err != nil {
		log.Fatal(err)
	}

	// 实现同步调用
	args := &Args{3, 4}
	var reply float64
	err = client.Call("ServiceA.Square", args, &reply)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("ServiceA.Square: reply: %f\n", reply)

	// 实现异步调用效果
	args2 := &Args{12, 16}
	var reply2 float64
	divCall := client.Go("ServiceA.Square", args2, &reply2, nil)
	replyCall := <-divCall.Done
	fmt.Println("error: ", replyCall.Error)
	fmt.Printf("ServiceA.Square: reply2: %f\n", reply2)
}
