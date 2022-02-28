package main

import "fmt"

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

func channel_demo() {
	ch := make(chan int)
	wg.Add(2)
	go channel_recv_demo(ch)
	go channel_send_demo(ch)
}
