package main

import "fmt"

func pointer() {
	text := `python是世界上最好的语言`
	a := text             // 取变量的名称
	b := &text            // &取变量的地址
	fmt.Println(a, b, *b) // *取地址对应的值

	var p *int
	p = new(int)
	*p = 100

	fmt.Printf("创建指针，并new初始化地址：%v, 得到值：%v", p, *p)

}
