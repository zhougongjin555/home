package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

type Param struct {
	// 传递指针的好处
	// 当字段required时，可以避免由于前端传递字段零值时候被gin框架误认为未传递字段

	ID      int     `json:"-"`
	Name    *string `json:"name" binding:"required"`
	Age     *int    `json:"age" binding:"required"`
	Married *bool   `json:"married" binding:"required"`
}

// ApiModel 把我数据库里面可以对外展示的字段放这里
type ApiModel struct {
}

// kind

func testHandler(c *gin.Context) {
	// 参数获取与参数校验
	var p Param
	if err := c.ShouldBind(&p); err != nil {
		fmt.Println(err)
		c.JSON(http.StatusOK, "参数错误:"+err.Error())
		return
	}
	// 获取到有效的参数
	fmt.Printf("p:%#v\n", p)

	var p2 Param
	age := 18
	p2.Age = &age

	// 返回响应
	c.JSON(http.StatusOK, p)
}
