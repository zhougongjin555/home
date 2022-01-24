package main

import "fmt"

type cal func(x string, y string) string

func add(a string, b string) string {
	return a + b
}

func f1() {
	//name := "zhugeliang"
	//fmt.Println(name)

	//var x cal // 定义变量，但是没有初始化，所以x == nil
	//fmt.Printf("未初始化：%T, %#v, %p\n", x, x, &x)
	//fmt.Println(x == nil)
	//x = add
	//fmt.Printf("初始化之后：%T, %#v, %p\n", x, x, &x)

	// 函数内部不能再次定义函数，除非
	// 1，匿名函数：不指定函数名、定义匿名函数赋值
	//f2 := func() {
	//	fmt.Println("我是大sb")
	//}
	//f2()
	//
	//// 2，定义匿名函数后立即执行
	//func() { fmt.Println("hello world") }()

	a := f2(3)
	b := a(4)
	for i := 0; i < 10; i++ {
		b = a(1)
	}
	fmt.Printf("累加10次结果：%d\n", b)

	f3()
}

func f2(x int) func(y int) int {
	f := func(y int) int {
		x += y
		return x
	}
	return f
}

func calc(index string, a, b int) int {
	ret := a + b
	fmt.Println(index, a, b, ret)
	return ret
}

func f3() {
	x := 1
	y := 2
	defer calc("AA", x, calc("A", x, y))
	x = 10
	defer calc("BB", x, calc("B", x, y))
	y = 20
	fmt.Println(x, y)
}
