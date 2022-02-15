package main

import "fmt"

type student struct {
	name string
	age  int8
}

func (s student) dream() {
	fmt.Println("不上班")
}
func interface_demo() {
	// 接口类型，只要实现了接口里面的方法，就认为实现了此类型的接口
	type dreamer interface {
		dream()
	}
	var s1 = student{"zhougongjin", 18}
	var d1 dreamer // 结构体s1里面实现了dream方法，可以赋值给接口。
	d1 = s1
	d1.dream()
}
