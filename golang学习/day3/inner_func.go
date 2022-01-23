package main

import "fmt"

func f4() {
	defer func() {
		e := recover()
		fmt.Printf("业务逻辑+报错信息：%s", e)
	}()

	defer func() {
		fmt.Println("defer 先行执行！！")
	}()

	var map3 map[string]int
	map3["age"] = 13

}
