package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func ginDemo1() {
	r := gin.Default() // 设置默认的路由引擎

	// 测试get请求
	r.GET("/index", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "get",
		})
	})
	// 测试post请求
	r.POST("/index", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "post",
		})
	})
	// 测试put请求
	r.PUT("/index", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "put",
		})
	})
	// 测试delete请求
	r.DELETE("/index", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "delete",
		})
	})
	r.Run(":8888") // 启动服务
}
