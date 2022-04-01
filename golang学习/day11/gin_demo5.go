/*gin框架绑定结构体字串*/
package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

type StructA struct {
	FieldA string `form:"field_A"`
}

type StructB struct {
	NextStruct StructA
	FieldB     string `form:"field_B"`
}

type StructC struct {
	NextStructPointer *StructB
	FieldC            string `form:"field_C"`
}

type StructD struct {
	NextAnonyStruct struct {
		FieldX string `form:"field_X"`
	}
	FieldD string `form:"field_D"`
}

func GetDataB(c *gin.Context) {
	// 将结构体中的数据返回给前端页面展示
	var b StructB
	c.Bind(&b)
	c.JSON(http.StatusOK, gin.H{
		"a": b.NextStruct,
		"b": b.FieldB,
		"c": b.NextStruct.FieldA,
	})
}

func GetDataC(c *gin.Context) {
	var sc StructC
	c.Bind(&sc)
	c.JSON(http.StatusOK, gin.H{
		"a": sc.FieldC,
		"b": sc.NextStructPointer,
		//"c": sc.NextStructPointer.FieldB,    // 如果未初始化赋值，那么就不能调用.FieldB，因为空值没有FieldB字段
	})
}

func GetDataD(c *gin.Context) {
	var d StructD
	c.Bind(&d)
	c.JSON(http.StatusOK, gin.H{
		"a": d.FieldD,
		"b": d.NextAnonyStruct,
		"c": d.NextAnonyStruct.FieldX,
	})
}

func ginDemo5() {

	var a = StructA{"周公瑾"}
	var b = StructB{a, "诸葛亮"}
	var c = StructC{&b, "刘玄德"}
	fmt.Printf("%#v\n", c)

	router := gin.Default()

	router.GET("/fieldb", GetDataB)
	router.GET("/fieldc", GetDataC)
	router.GET("/fieldd", GetDataD)

	router.Run(":8888")

}
