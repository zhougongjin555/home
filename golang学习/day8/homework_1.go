package main

import (
	"fmt"
	"math/rand"
	"strconv"
	"sync"
	"time"
)

type res struct {
	num int
	sum int
}

// 创建产生随机数的函数
func create_rand_number() (rand_num int) {
	//seed := time.Now().UnixNano()
	//rand.Seed(seed)
	//fmt.Println(seed)
	rand_num = rand.Intn(99999)
	return
}

// 计算随机数各位之和的函数
func generate_sum_rand(number int) (sumNum int) {
	numStr := strconv.Itoa(number) // 把int类型转换为string
	numStrSlice := []rune(numStr)  // 把字符串转为rune类型
	// 计算num各个位数的和
	for _, numInt := range numStrSlice {
		number, _ = strconv.Atoi(string(numInt))
		sumNum += number
	}
	return
}

// 计算随机数各位之和发送给resultChan,并打印
func run(num int) {
	var wg sync.WaitGroup

	jobChan := make(chan int, 24)
	resultChan := make(chan res, 24)
	wg.Add(1)
	go func() {
		for i := 0; i < num; i++ {
			jobChan <- create_rand_number()
		}
		wg.Done()
		close(jobChan)
	}()

	go func() {
		for i := 0; i < 24; i++ {
			wg.Add(1)
			go func() {
				for v1 := range jobChan {
					r := res{
						num: v1,
					}
					v2 := generate_sum_rand(v1)
					r.sum = v2
					resultChan <- r
				}
				wg.Done()
			}()
		}
		wg.Wait()
		close(resultChan)
	}()

	for i := range resultChan {
		fmt.Printf("数字:%d 和:%d\n", i.num, i.sum)
		time.Sleep(time.Second)
	}
}
