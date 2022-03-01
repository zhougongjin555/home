package main

import (
	"fmt"
	"math/rand"
	"strconv"
	"time"
)

func producer(jobch chan int64) <-chan int64 {
	for i := 0; i < 100; i++ {
		num := rand.Int63()
		jobch <- num
		fmt.Println("随机数：", num)
		time.Sleep(time.Millisecond * time.Duration(200))
	}
	wg.Done()
	return jobch
}

func worker(jobch chan int64, resch chan int16) <-chan int16 {
	for val := range jobch {
		res := cal(val)
		resch <- res
	}
	wg.Done()
	return resch
}

func cal(dat int64) int16 {
	str := strconv.Itoa(int(dat))
	sum := 0
	for _, s := range str {
		val, _ := strconv.Atoi(string(s))
		sum += val
	}
	return int16(sum)
}

func work() {
	jobch := make(chan int64, 10)
	resch := make(chan int16, 10)
	wg.Add(2)
	go producer(jobch)
	go worker(jobch, resch)
	for {
		select {
		case res := <-resch:
			fmt.Println(res)
		case jobnum := <-jobch:
			rest := cal(jobnum)
			resch <- rest
		case <-time.After(time.Second * time.Duration(3)): // 十秒无内容取出，超时退出
			fmt.Println("超时退出")
			return
		}
	}
}
