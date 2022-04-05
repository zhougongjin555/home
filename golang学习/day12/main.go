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
	gormDemo()
}
