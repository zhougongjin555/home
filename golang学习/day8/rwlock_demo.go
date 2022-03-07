package main

import (
	"fmt"
	"sync"
	"time"
)

var rwm sync.RWMutex

func addfunc() {
	rwm.Lock()              // 写锁
	time.Sleep(time.Second) // 写假设耗时1s
	fmt.Println("写...")
	rwm.Unlock()
	wg.Done()
}

func getfunc() {
	rwm.RLock()                  // 读锁
	time.Sleep(time.Millisecond) // 读耗时1ms
	fmt.Println("读...")
	rwm.RUnlock()
	wg.Done()
}

func rwlock_demo() {
	wtimes := 10
	rtimes := 100
	num := 1
	for i := 0; i < wtimes; i++ {
		wg.Add(num)
		go addfunc()
	}
	for j := 0; j < rtimes; j++ {
		wg.Add(1)
		go getfunc()
	}

}
