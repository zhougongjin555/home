package main

import (
	"fmt"
)

type reader interface {
	Read()
	Close()
}
type writer interface {
	Write()
	Close()
}
type readwriter interface { // 结构体嵌套语法
	reader
	writer
}

type Person struct {
	name string
}

func (ps *Person) Read() {
	fmt.Println("读取...")
}

func (ps *Person) Write() {
	fmt.Println("写入...")
}

func (ps *Person) Close() {
	fmt.Println("关闭...")
}

func demo2() {
	var p = &Person{"周公瑾"}
	//p.Read()
	//p.Write()
	var rw readwriter
	rw = p
	rw.Read()
	rw.Write()
	rw.Close()
}
