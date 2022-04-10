package main

import "github.com/gin-gonic/gin"

func main() {

	r := gin.Default()

	r.POST("/api/test", testHandler)
	r.Run(":8911")
}
