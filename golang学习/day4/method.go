package main

import "fmt"

type People struct {
	name string
	age  int
}

type MyString string

// 结构体方法
func (p People) dream(s string) {
	fmt.Printf("%s dream is %s", p.name, s)
}

// 自定义类型方法
func (ms MyString) SayHello() {
	fmt.Println("\nhello, world, i'm zhougongjin")
}

func demo2() {
	p := People{"周公瑾", 22}
	p.dream("rich")
	var ms1 MyString
	ms1.SayHello()
}
