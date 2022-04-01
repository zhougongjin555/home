/*gin 框架从query、body、json、path中获取参数*/
package main

import (
	"encoding/json"
	"github.com/gin-gonic/gin"
	"net/http"
)

type LoginForm struct { // post参数结构体
	Usr string `form:"username" binding: "required"`
	Pwd string `form:"password" binding: "required"`
}

func ginDemo3() {
	router := gin.Default()
	// 获取get请求query中的参数
	router.GET("/login", func(c *gin.Context) {
		//username := c.Query("username") // 直接从url的query中获取参数
		//password := c.Query("password")
		username := c.DefaultQuery("username", "周公瑾") // 尝试从query中获取参数，如果没有设置为后面的默认值
		password := c.DefaultQuery("password", "zhouzhou123")
		c.JSON(200, gin.H{
			"username": username,
			"password": password,
		})
	})

	// 获取post请求体中的参数1
	router.POST("/register", func(c *gin.Context) {
		// DefaultPostForm取不到值时会返回指定的默认值
		//username := c.DefaultPostForm("username", "小王子")
		username := c.PostForm("username")
		address := c.PostForm("address")
		//输出json结果给调用方
		c.JSON(http.StatusOK, gin.H{
			"message":  "ok",
			"username": username,
			"address":  address,
		})
	})

	// 获取post请求体中的参数2---参数绑定
	router.POST("/login", func(c *gin.Context) {
		var form LoginForm
		if c.ShouldBind(&form) == nil {
			if form.Usr == "zhougongjin" && form.Pwd == "zhouzhou123" {
				c.JSON(http.StatusOK, gin.H{"status": "welcome to go: " + form.Usr})
			} else {
				c.JSON(http.StatusNonAuthoritativeInfo,
					gin.H{"status": "username or password wrong"})
			}
		}
	})

	// 从请求体中的json串中解析参数信息
	router.POST("/json", func(c *gin.Context) {
		b, err := c.GetRawData() // 从c.request.body中读取请求数据
		if err != nil {
			panic(err)
		}
		var m map[string]interface{}
		// json反序列化数据
		err = json.Unmarshal(b, &m) // 传递指针参能实现对值的修改操作
		if err != nil {
			panic(err)
		}
		c.JSON(http.StatusOK, m)
	})

	// 获取path中的参数      :str 字符串占位
	router.GET("/index/static/:path/:file", func(c *gin.Context) {
		path := c.Param("path")
		file := c.Param("file")
		c.JSON(http.StatusOK, gin.H{
			"path": path,
			"file": file,
		})
	})

	router.Run(":8888")
}
