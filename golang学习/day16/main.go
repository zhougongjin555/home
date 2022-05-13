package main

func main() {
	//RpcDemo()

	// RESTful API
	//http.HandleFunc("/square", SquareHandler)
	//log.Fatal(http.ListenAndServe(":8888", nil))

	// RPC
	// 基于Http服务的rpc
	//RpcHttp()
	// 基于TCP服务的rpc
	//RpcTcp()
	// 基于protoc实现自动生成文件的微服务
	//ProtocDemo()
	// 基于grpc实现微服务
	GRpcDemo()
}
