package main

import (
	"encoding/json"
	"fmt"
)

type student struct {
	Name string // 大写可以被识别
	age  int    // 小写无法被访问，所以就无法被识别
}

func demo2() {
	s1 := student{"zhougongjin", 18}
	b, err := json.Marshal(s1)
	if err != nil {
		fmt.Println("序列化失败")
		return
	}
	fmt.Printf("%s", b)
}
