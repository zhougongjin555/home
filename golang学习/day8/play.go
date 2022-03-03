package main

import (
	"fmt"
)

func play() {
	wg.Add(1)
	go func() {
		fmt.Println("进入函数2")
		wg.Done()
	}()

	go func() {
		fmt.Println("进入函数1外层")
		for i := 0; i < 10; i++ {
			wg.Add(1)
			go func(n int) {
				fmt.Println("进入内层", n)
				wg.Done()
			}(i)
		}
	}()

	//time.Sleep(time.Second)
	wg.Wait()

	fmt.Println("执行主函数")
}
