// 基于RPC实现数据传输
package main

import (
	"log"
	"math"
	"net"
	"net/rpc"
)

// 定义微服务接受的全部参数
type Args struct {
	X, Y float64
}

// 创建一个空结构体实现微服务
type ServiceA struct {
}

func (s *ServiceA) Square(args *Args, reply *float64) error {
	// 参数里面实现接收参数的指针，以及返回值的指针，后面赋值直接取地址赋值
	*reply = math.Sqrt(math.Pow(args.X, 2) + math.Pow(args.Y, 2))
	return nil
}

func RpcTcp() {
	service := new(ServiceA) // 实例化空结构体
	rpc.Register(service)    // 为结构体注册微服务
	l, err := net.Listen("tcp", ":9999")
	if err != nil {
		log.Fatal(err)
	}
	for { //
		conn, _ := l.Accept()
		rpc.ServeConn(conn)
	}

}
