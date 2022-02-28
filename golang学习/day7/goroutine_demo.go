package main

import (
	"fmt"
)

func f1() {
	fmt.Print("符号看象限\n")
	wg.Done()
}

func f2() {
	fmt.Print("三角函数：\n")
	wg.Done()
}

func goroutine_demo() {
	//for i := 0; i < 1000; i++ {
	//	wg.Add(1)
	//	go f2()
	//}
	wg.Add(2)
	go f2()
	go f1()
	fmt.Print("奇变偶不变\n")
	//time.Sleep(time.Second) // 如果不等待，那么主函数运行完成，直接结束进程，上面的函数可能还没执行完成
}
