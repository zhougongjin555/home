// 基于RESTful API规范的数据传输方式
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"net/rpc"
)

type RecvParams struct {
	X float64 `json:"X"`
	Y float64 `json:"y"`
}

type SendParams struct {
	Code int16   `json:"code"`
	Z    float64 `json:"z"`
}

func SquareHandler(w http.ResponseWriter, r *http.Request) {
	b, _ := ioutil.ReadAll(r.Body)
	var recv RecvParams
	json.Unmarshal(b, &recv)
	fmt.Printf("json 解析得到数据：%#v\n", recv)
	ret := square(recv.X, recv.Y)
	respBytes, err := json.Marshal(SendParams{Code: 200, Z: ret})
	if err != nil {
		panic(err)
	}
	w.Write(respBytes)
	fmt.Println("服务器成功返回数据", ret)
}

func RpcHttp() {
	service := new(ServiceA) // 实例化空结构体
	rpc.Register(service)    // 为结构体注册微服务

	// 基于http服务的RPC
	rpc.HandleHTTP()
	l, err := net.Listen("tcp", ":9999")
	if err != nil {
		panic(err)
	}
	http.Serve(l, nil)
}
