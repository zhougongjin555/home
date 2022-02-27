package main

import (
	"sync"
)

var wg sync.WaitGroup

func main() {
	//time_demo()
	//goroutine_demo()
	channel_demo()
	wg.Wait()
}
