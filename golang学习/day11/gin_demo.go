package main

import "github.com/gin-gonic/gin"

func ginDemo1() {
	r := gin.Default()
	r.GET("/hello", func(c *gin.Context) {
		// c.JSON：返回JSON格式的数据
		c.JSON(200, gin.H{
			"message": "Hello world!",
		})
	})
	r.Run(":8080")
}
