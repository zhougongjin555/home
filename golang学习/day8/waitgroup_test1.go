package main

import (
	"fmt"
)

func test1(num int) {
	wg.Add(num)
	for i := 0; i < 10; i++ {
		go func() {
			fmt.Printf("米奇妙妙屋\n")
			wg.Done()
		}()
	}
	wg.Done()
}

func wg_test() {
	num := 10
	wg.Add(1)
	go test1(num)
}
