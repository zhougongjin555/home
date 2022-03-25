package main

import (
	"encoding/json"
	"fmt"
)

type student struct {
	ID     int
	Gender string
	Name   string
}

type class struct {
	Title   string
	Student []*student // !!! 指针类型的字段只能接受指针类型的变量，普通字段只能接受普通类型的变量
}

func demo4() {
	s1 := &student{1, "male", "周公瑾"}             // 创建指针类型的变量
	c := &class{"111", make([]*student, 0, 100)} // make(slice, len, cap)，初始化长度为0，容量为100的切片
	//fmt.Printf("%v  %v", len(c.student), cap(c.student))
	c.Student = append(c.Student, s1)
	fmt.Printf("c: %#v\n", c)

	// json 序列化
	data, err := json.Marshal(c)
	if err != nil {
		fmt.Print("json.Marshal failed")
		return
	}
	fmt.Printf("序列化：%s, %#v\n", data, c.Student)

	// json 反序列化
	str := `{"Title":"101","Student":[{"ID":0,"Gender":"男","Name":"stu00"},{"ID":1,"Gender":"男","Name":"stu01"},{"ID":2,"Gender":"男","Name":"stu02"},{"ID":3,"Gender":"男","Name":"stu03"},{"ID":4,"Gender":"男","Name":"stu04"},{"ID":5,"Gender":"男","Name":"stu05"},{"ID":6,"Gender":"男","Name":"stu06"},{"ID":7,"Gender":"男","Name":"stu07"},{"ID":8,"Gender":"男","Name":"stu08"},{"ID":9,"Gender":"男","Name":"stu09"}]}`
	c1 := &class{}
	err = json.Unmarshal([]byte(str), c1)
	if err != nil {
		fmt.Println("json unmarshal failed!")
		return
	}
	fmt.Printf("反序列化：%#v, Title: %s, Students: %p\n", c1, c1.Title, c1.Student)
	for _, student := range c1.Student {
		fmt.Println(student.ID, student.Name, student.Gender)
	}

}
