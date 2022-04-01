/*gin框架的单文件上传和多文件上传, 以及日志写入*/
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"io"
	"net/http"
	"os"
	"strings"
)

func ginDemo4() {
	gin.DisableConsoleColor() // 禁用控制台颜色，将日志写入文件时不需要控制台颜色。
	// 日志记录到文件
	f, _ := os.Create("gin.log")
	gin.DefaultWriter = io.MultiWriter(f)

	router := gin.Default()
	// 上传单文件
	router.POST("/upload", func(c *gin.Context) {
		file, err := c.FormFile("file") // 从表单中提取file文件
		if err != nil {
			panic(err)
		}
		fmt.Println(file.Filename)

		dst := "./files/" + file.Filename // 文件保存路径
		fmt.Println(dst)
		c.SaveUploadedFile(file, dst) // 保存文件到指定路径

		c.String(http.StatusAccepted, fmt.Sprintf("'%s' uploaded!", file.Filename))
	})

	// 上传多个文件
	router.MaxMultipartMemory = 2 << 20 // 设置为最大1mb大小
	router.POST("/uploads", func(c *gin.Context) {
		var name []string
		form, _ := c.MultipartForm()
		files := form.File["files"] // form 表单中的上传文件字段参数
		// 遍历文件切片获得每一个文件
		for idx, file := range files {
			fmt.Println(idx, file.Filename)
			name = append(name, file.Filename)
			dst := "./files/" + file.Filename // 文件保存路径
			c.SaveUploadedFile(file, dst)
		}

		c.JSON(http.StatusOK, gin.H{
			"message": "files uploaded",
			"detail":  strings.Join(name, "、"), // 前面的参数是用来拼接的字符串切片，后面的参数是分隔符
		})
	})

	router.Run(":8888")
}
