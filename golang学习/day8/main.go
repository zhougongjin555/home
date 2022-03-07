package main

import (
	"fmt"
	"sync"
	"time"
)

var (
	wg sync.WaitGroup
)

func main() {
	start := time.Now()
	//lock_demo()
	//rwlock_demo()
	//demo1()
	//homework()
	//goroutine_demo1()
	//wg_test()
	sync_map_demo()

	wg.Wait()
	//fmt.Println(x)
	//fmt.Println("执行到main函数")
	cost := time.Since(start)
	fmt.Println(cost)
}
