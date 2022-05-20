// grpc对应的客户端
package main

import (
	"context"
	"flag"
	"fmt"
	"google.golang.org/grpc"
	"log"
	pb "myclient/address" // 导入地址应该与init时候使用的名称一致，并不能使用文件夹路径
	"time"
)

var (
	addr = flag.String("addr", "127.0.0.1:9999", "the address to connect to")
	id   = flag.Int("id", 1, "student Id")
	name = flag.String("name", "周公瑾", "student Name")
	age  = flag.Int("age", 22, "student Age")
)

func ClientDemo4() {
	flag.Parse()
	// 连接到server端
	conn, err := grpc.Dial(*addr, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	// 为grpc连接新建一个服务
	by := pb.NewBirthYearServiceClient(conn)
	ty := pb.NewTwoAfterYearAgeServiceClient(conn)

	// Contact the server and print out its response.
	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()
	x, _ := by.BirthYear(ctx, &pb.StudentRequest{Id: int32(*id), Name: *name, Age: int32(*age)})
	y, _ := ty.TwoAfterYearAge(ctx, &pb.StudentRequest{Name: *name})

	fmt.Println("BirthYear: ", x)
	fmt.Println("TwoAfterYearAge: ", y)
}
