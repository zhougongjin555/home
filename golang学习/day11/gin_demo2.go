/*HTML渲染*/
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

func ginDemo2() {
	router := gin.Default()
	router.LoadHTMLGlob("templates/*") // 指定html目录
	//router.LoadHTMLFiles("templates/404.html")  // 直接指定文件

	router.NoRoute(func(c *gin.Context) {
		c.HTML(http.StatusOK, "404.html", gin.H{
			"title": "404 website",
		})
	})
	fmt.Println()
	router.Run(":8888")
}
