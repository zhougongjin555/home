// 使用JSON协议的rpc, 方便跨语言进行数据传输
package main

import (
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"
)

func RpcJsonDemo() {
	service := new(ServiceA)
	rpc.Register(service)
	l, err := net.Listen("tcp", ":9999")
	if err != nil {
		panic(err)
	}
	for {
		conn, _ := l.Accept()
		rpc.ServeCodec(jsonrpc.NewServerCodec(conn))
	}
}
