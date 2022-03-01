package main

import (
	"fmt"
	"strconv"
)

//var ch chan int

func channel_send_demo(ch chan int) {
	send1 := 60
	ch <- send1
	fmt.Println("发送值:", send1)
	wg.Done()
}

func channel_recv_demo(ch chan int) {
	recv := <-ch
	fmt.Println("接收到值:", recv)
	wg.Done()
}

func recvall(ch chan string) {
	// 多返回值
	//for {
	//	value, ok := <-ch
	//	fmt.Println(value)
	//	if !ok {
	//		fmt.Println("通道被关闭，sleeping...")
	//		break
	//	}
	//}
	for value := range ch {
		fmt.Println("从通道拿到数值:", value)
	}
	wg.Done()
}

func channel_demo() {
	//ch := make(chan int)
	//wg.Add(2)
	//go channel_recv_demo(ch)
	//go channel_send_demo(ch)
	sCh := make(chan string, 3)
	wg.Add(1)
	go recvall(sCh)

	for i := 0; i < 10; i++ {
		sCh <- strconv.Itoa(i)
	}
	close(sCh)
}
