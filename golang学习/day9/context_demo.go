package main

import (
	"context"
	"fmt"
	"math/rand"
	"time"
)

func worker1(ctx context.Context) {
	// 每秒产生一个随机数并打印直到收到停止信号，退出死循环
WORK:
	for {
		num := rand.Intn(999)
		fmt.Println("我是worker1, 我产生了个随机数：", num)
		time.Sleep(time.Second)
		select {
		case <-ctx.Done():
			break WORK
		default:
		}
	}
	wg.Done()
}

func worker2(ctx context.Context) {
	// 每秒产生一个随机数并打印直到收到停止信号，退出死循环
WORK:
	for {
		num := rand.Intn(888)
		fmt.Println("我是worker2, 我产生了个随机数：", num)
		time.Sleep(time.Second)
		select {
		case <-ctx.Done():
			break WORK
		default:
		}
	}
	wg.Done()
}

func context_demo() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel() // WithCancel调用后在上下文运行操作完成后应该立即调用cancel

	wg.Add(2)
	go worker1(ctx)
	go worker2(ctx)
	time.Sleep(time.Second * 10)

}
