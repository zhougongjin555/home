package main

import (
	"fmt"
	"reflect"
)

var slice1 []int

func f1() {
	//b := a[1:3]
	//数组赋值
	//slice1[0] = 100
	//aa := 100
	//slice1[10] = aa
	// 切片扩容内存地址会发生变化
	fmt.Println(slice1, len(slice1), cap(slice1))
	fmt.Printf("老地址%p\n", &slice1)
	slice2 := append(slice1, 1, 2, 3)
	fmt.Println(slice2, len(slice2), cap(slice2))
	fmt.Printf("新地址%p\n", &slice2)

	var str = "zhougongjin"
	str_s := str[:4]
	fmt.Println(str_s, reflect.TypeOf(str_s), reflect.TypeOf(str))

	var arr6 = [10]int{1, 2, 3, 4, 5}
	slice3 := arr6[1:4]
	slice4 := slice3[1:4]
	fmt.Printf("数组:%p, 切片1:%p, 切片2:%p\n", &arr6[2], &slice3[1], &slice4[0])
	fmt.Println(slice3, len(slice3), cap(slice3))
	fmt.Println(slice4, len(slice4), cap(slice4))

	// make空切片不是nil，因为初始化过了
	var slice5 []int
	var slice6 []int
	{
	}
	var slice7 = make([]int, 0)
	fmt.Println(slice5 == nil, slice6 == nil, slice7 == nil) // false

	slice8 := []int{1, 2, 3}
	slice9 := make([]int, 10, 100)
	copy(slice9, slice8)
	slice9[1] = 100
	fmt.Println(slice9, slice8)

	var slice10 = []string{"a", "b", "c"}
	fmt.Printf("%+v,%p,%p %p\n", slice10, &slice10[0], &slice10[1], &slice10[2])
	var slice11 = []string{"周", "公", "瑾"}
	fmt.Printf("%+v,%p,%p %p\n", slice11, &slice11[0], &slice11[1], &slice11[2])
	var slice12 = []int{1, 2, 3}
	fmt.Printf("%+v,%p,%p %p\n", slice12, &slice12[0], &slice12[1], &slice12[2])

	var a = make([]string, 5, 10)
	var b []int
	fmt.Println(a)
	for i := 0; i < 10; i++ {
		b = append(b, i)
		a = append(a, fmt.Sprintf("%v", i))
	}
	fmt.Println(a, len(a), cap(a))
	fmt.Println(b, len(b), cap(b))

}
