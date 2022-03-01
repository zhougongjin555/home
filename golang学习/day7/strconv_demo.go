package main

import (
	"fmt"
	"reflect"
	"strconv"
)

func strconv_demo() {
	// str ==> int
	str1 := "100"
	dat1, err := strconv.Atoi(str1)
	if err != nil {
		fmt.Println("conv error")
		return
	}
	fmt.Printf("转换后的数字： %d, %v\n", dat1, reflect.TypeOf(dat1))

	// int ==> str
	str2 := strconv.Itoa(dat1)
	fmt.Printf("转换后的字符： %s, %v\n", str2, reflect.TypeOf(str2))

	// str ==> bool, int, uint(无符号整数), float
	str3 := "t"
	fmt.Println(strconv.ParseBool(str3))
	str4 := "123.45"
	fmt.Println(strconv.ParseFloat(str4, 32)) // 指定32位，64位小数

	// bool, int, uint, float ==> str
	bool1 := true
	fmt.Println(strconv.FormatBool(bool1))
	var int1 int64 = 2003325
	fmt.Println(strconv.FormatInt(int1, 10)) // 需要指定进制，2---36进制
	var float1 float64 = 123.456
	fmt.Println(strconv.FormatFloat(float1, 'f', 3, 64)) // 指定fmt格式，精度，位数

}
