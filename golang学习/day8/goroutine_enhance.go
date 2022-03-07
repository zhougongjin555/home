package main

import (
	"fmt"
	"time"
)

func demo1() {
	go func() {
		fmt.Println("执行到外部goroutine函数了")
		wg.Add(1)

		go func() {
			fmt.Println("执行到内部goroutine函数了")
			for i := 0; i < 3; i++ {
				fmt.Printf("内部函数打印%d\n", i)
			}
			wg.Done()
		}()

		wg.Wait()
	}()

	time.Sleep(100)
	fmt.Println("执行到主函数了")
}
