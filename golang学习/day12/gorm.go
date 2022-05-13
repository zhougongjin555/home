package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	Nickname string
	Username string `gorm:"not null; unique"`
	Password string `gorm:"not null"`
}

type Todo struct {
	gorm.Model
	Uid    *int64  `form:"uid" binding:"required" `   // 所属用户
	Title  *string `form:"title" binding:"required"`  // 待办事项名称
	Status *bool   `form:"status" binding:"required"` // 是否完成的状态
}

type FromTodo struct {
	Uid    int64
	Title  string
	Status bool
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
	//user := User{Nickname: "关关", Username: "guanyunchang", Password: "guanguan123"}
	//result := db.Create(&user)
	//c.JSON(200, gin.H{
	//	"error":        result.Error,
	//	"id":           user.ID,
	//	"RowsAffected": result.RowsAffected,
	//})

	var todo Todo
	if err := c.ShouldBind(&todo); err != nil {
		panic(err)
	}
	fmt.Printf("%#v", todo)
	result := db.Create(&todo)
	c.JSON(200, gin.H{
		"error":        result.Error,
		"id":           todo.ID,
		"RowsAffected": result.RowsAffected,
	})
}

// updateTodoHandler 更新待办事项
func updateTodoHandler(c *gin.Context) {
	c.JSON(200, "updateTodoHandler")
}

// getTodoHandler 获取所有待办事项
func getTodoHandler(c *gin.Context) {
	var todo FromTodo
	//// 获取首条数据
	//db.Model(&Todo{}).First(&todo)
	//fmt.Printf("first--id: %d, title: %s, title: %t\n", todo.Uid, todo.Title, todo.Status)
	//
	//// 随机获取一条数据
	//db.Model(&Todo{}).Take(&todo)
	//fmt.Printf("take--id: %d, title: %s, title: %t\n", todo.Uid, todo.Title, todo.Status)
	//
	//// 获取最后一条数据
	//last := db.Model(&Todo{}).Last(&todo)
	//if errors.Is(last.Error, gorm.ErrRecordNotFound) {
	//	panic(last.Error)
	//}
	//fmt.Printf("last--id: %d, title: %s, title: %t\n", todo.Uid, todo.Title, todo.Status)
	//
	//// 按条件查询，默认查询条件是主键
	db.Model(&Todo{}).Find(&todo, 3)
	fmt.Printf("按主键值查询--id: %d, title: %s, title: %t\n", todo.Uid, todo.Title, todo.Status)

	var todos []FromTodo                           // 查询全部的记录
	db.Model(&Todo{}).Find(&todos, []int{2, 3, 4}) // where id in [...]
	fmt.Printf("按主键区间查询--%#v\n", todos)

	db.Model(&Todo{}).Where(&todo, "title=?", "手冲")
	fmt.Printf("按指定字段查询--id: %d, title: %s, title: %t\n", todo.Uid, todo.Title, todo.Status)

	c.JSON(200, gin.H{
		//"error":  last.Error,
		"title":  todo.Title,
		"status": todo.Status,
		"uid":    todo.Uid,
	})
}

// deleteTodoHandler 删除待办事项
func deleteTodoHandler(c *gin.Context) {
	c.JSON(200, "deleteTodoHandler")
}
