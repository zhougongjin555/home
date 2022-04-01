/*gin框架自定义中间件*/
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"time"
)

func MyMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		t := time.Now()
		c.Set("name", "周公瑾")
		c.Next() // 走向下一个中间件执行

		// 计算请求耗时
		cost := time.Since(t)
		fmt.Println("请求共耗时： ", cost)

		status := c.Writer.Status()
		fmt.Println("请求状态码： ", status)

	}
}

func ginDemo6() {
	//r := gin.New() // 使用空白引擎，方便查看中间件的效果
	r := gin.Default()
	r.Use(MyMiddleware())

	r.GET("/test", func(c *gin.Context) {
		example := c.MustGet("name").(string)
		time.Sleep(time.Second)

		// 打印："12345"
		fmt.Println(example)
	})

	// 监听并在 0.0.0.0:8080 上启动服务
	r.Run(":8888")
}
