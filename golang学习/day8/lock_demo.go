package main

import (
	"sync"
)

var (
	x int64
	m sync.Mutex
)

// add 对全局变量x执行5000次加1操作
func add() {
	for i := 0; i < 5000; i++ {
		m.Lock() // 修改x前加锁
		x = x + 1
		m.Unlock() // 改完解锁
	}
	wg.Done()
}

func lock_demo() {
	wg.Add(2)
	go add()
	go add()
}
