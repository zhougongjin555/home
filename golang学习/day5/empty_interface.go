package main

import "fmt"

type Any interface {
	// 定义空接口
}

func demo3() {
	var a Any // 空接口可以接受任何类型的变量，鸭子类型
	a = "公瑾"
	fmt.Printf("我的名字：%v\n", a)
	a = 10
	fmt.Printf("我的年龄：%d\n", a)
	a = true
	fmt.Printf("我是男的？%t\n", a)
}
