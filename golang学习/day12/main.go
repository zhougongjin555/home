package main

import "fmt"

func main() {
	// 连接数据库
	if err := initDB(); err != nil {
		fmt.Println("connect mysql failed", err)
		panic(err)
	}
	// 表结构
	db.AutoMigrate(&Todo{})
	db.AutoMigrate(&User{})
	gormDemo()

	//type uu struct {
	//	a *int8
	//}
	//var b int8 = 16
	//var c int8 = 32
	//u := uu{}
	//u.a = &b
	//fmt.Print(*u.a)
	//
	//u.a = &c
	//fmt.Print("\n", *u.a)
}
