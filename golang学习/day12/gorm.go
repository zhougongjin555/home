package main

import (
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type Todo struct {
	gorm.Model
	Title  string // 待办事项名称
	Status bool   // 是否完成的状态
}

func gormDemo() {
	r := gin.Default()

	// 注册路由，增删改查
	// 添加待办事项
	g := r.Group("/api/v1")
	{
		g.POST("/todo", createTodoHandler)
		g.PUT("/todo", updateTodoHandler)
		g.GET("/todo", getTodoHandler)
		g.DELETE("/todo", deleteTodoHandler)
	}

	// 启动http server端
	r.Run(":8888")
}

// createTodoHandler 创建待办事项
func createTodoHandler(c *gin.Context) {
	c.JSON(200, "createTodoHandler")
}

// updateTodoHandler 更新待办事项
func updateTodoHandler(c *gin.Context) {
	c.JSON(200, "updateTodoHandler")
}

// getTodoHandler 获取所有待办事项
func getTodoHandler(c *gin.Context) {
	c.JSON(200, "getTodoHandler")
}

// deleteTodoHandler 删除待办事项
func deleteTodoHandler(c *gin.Context) {
	c.JSON(200, "deleteTodoHandler")
}
