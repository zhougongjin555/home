package main

import (
	"github.com/gin-gonic/gin"
	"log"
)

// ApiModel 把我数据库里面可以对外展示的字段放这里
type ApiModel struct {
}

func GinServer() {
	ViperDemo()
	InitMyLogger()
	if err := MysqlInit(); err != nil {
		return
	}
	/*
		1, 初始化gin框架
		2, 绑定url与对应视图函数
		3, 启动gin框架
	*/
	r := gin.Default()
	r.POST("/books", createBookHandler)
	r.GET("/books", getBookHandler)
	r.PUT("/books", updateBookHandler)
	r.DELETE("/books", deleteBookHandler)
	err := r.Run(":9110")
	if err != nil {
		log.Fatalf("gin start error: %s", err)
	}
}
