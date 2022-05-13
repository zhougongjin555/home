package main

import (
	"fmt"
	"math"
)

// 计算斜边长
func square(x, y float64) float64 {
	return math.Sqrt(math.Pow(x, 2) + math.Pow(y, 2))
}

func RpcDemo() {
	var (
		a float64 = 3
		b float64 = 4
	)
	c := square(a, b)
	fmt.Println("斜边长度为：", c)

}
