package main

import (
	"fmt"
	"unsafe"
)

type MyInt int    //类型定义
type NewInt = int //类型别名

// 普通结构体
type Student struct {
	name    string
	age     int
	married bool
	sex     string
}

func demo1() {
	//var a MyInt = 100
	//var b NewInt = 100
	////fmt.Println(a == b)  // 类型别名只在源文件生效，编译时会自动替换成为原始类型
	//fmt.Printf("a:%T, b:%T", a, b)

	//var stu1 = Student{
	//	"周公瑾", 12, false, "man",
	//}
	//
	//fmt.Println(stu1)
	//fmt.Printf("name: %s, age: %d, married: %v, sex: %s", stu1.name, stu1.age, stu1.married, stu1.sex)

	//匿名结构体
	var person struct {
		name string
		age  int
	}
	person.name = "zhugeliang"
	person.age = 22
	fmt.Printf("\n%+v", person)

	//结构体指针
	stu2 := &Student{}
	(*stu2).name = "关云长" // 正常思路的赋值操作
	stu2.age = 23        // go提供的语言糖赋值操作
	stu2.married = true
	stu2.sex = "male"
	fmt.Printf("%+v\n", stu2)
	fmt.Println(unsafe.Alignof(stu2))
	fmt.Println(unsafe.Sizeof(stu2))

	type Bar struct {
		b int8  // 1
		a int32 // 4
		c int8  // 1
		d int64 // 8
	}

	var b1 Bar
	fmt.Println(unsafe.Alignof(b1), unsafe.Sizeof(b1)) // 24
}
