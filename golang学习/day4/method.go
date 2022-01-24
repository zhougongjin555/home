package main

import "fmt"

type People struct {
	name string
	age  int
}

// 方法
func (p People) dream(s string) {
	fmt.Printf("%s dream is %s", p.name, s)
}

func demo2() {
	p := People{"周公瑾", 22}
	p.dream("rich")
}
