package main

import (
	"fmt"
	"unsafe"
)

func demo3() {
	type Store1 struct {
		s1 int8  // 1
		s2 int16 // 2
		s3 int64 // 8
		s4 int8  // 2
		s5 int32 // 4
	}
	type Store2 struct {
		s1 int8  // 1
		s4 int8  //
		s2 int16 // 2
		s5 int32 // 4
		s3 int64 // 8
	}
	s1 := Store1{}
	s2 := Store2{}
	fmt.Println(unsafe.Sizeof(s1), unsafe.Sizeof(s2))

	store1 := Store1{11, 22, 33, 44, 55}
	fmt.Printf("struct:%p\n", &store1)
	fmt.Printf("s1:%p\n", &store1.s1)
	fmt.Printf("s2:%p\n", &store1.s2)
	fmt.Printf("s3:%p\n", &store1.s3)
	fmt.Printf("s4:%p\n", &store1.s4)
	fmt.Printf("s5:%p\n", &store1.s5)

	type ss1 struct {
		m struct{}
		n int
	}

	type ss2 struct {
		m int
		n struct{}
	}

	ss11 := ss1{}
	ss22 := ss2{}
	fmt.Printf("%p, %p\n", &ss11, &ss22)
	fmt.Printf("ss11.m:%p\n", &ss11.m)
	fmt.Printf("ss11.n:%p\n", &ss11.n)
	fmt.Printf("ss22.m:%p\n", &ss22.m)
	fmt.Printf("ss22.n:%p\n", &ss22.n)

	type student1 struct {
		name string
		age  int
	}
	m := make(map[string]*student1)
	stus := []student1{
		{name: "小王子", age: 18},
		{name: "娜扎", age: 23},
		{name: "大王八", age: 9000},
	}
	fmt.Printf("stus[2]: %p\n", &stus[2])
	for _, stu := range stus {
		fmt.Printf("stu: %p\n", &stu)
		m[stu.name] = &stu
		// 刻舟求剑
	}
	for k, v := range m {
		fmt.Println(k, "=>", v.name)
	}
}
