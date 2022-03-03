package main

import (
	"fmt"
	"math/rand"
	"time"
)

func push(ch chan int) <-chan int {
	go func() {
		for {
			select {
			case ch <- rand.Intn(9999):
			default:
				time.Sleep(time.Millisecond)
			}
		}
	}()
	return ch
}

func pull(ch chan int) {
	for {
		val, _ := <-ch
		fmt.Println("拿到值", val)
	}
}

func goroutine_demo1() {
	intCh := make(chan int, 16)
	go push(intCh)
	go pull(intCh)
	time.Sleep(time.Second * time.Duration(10))
}
