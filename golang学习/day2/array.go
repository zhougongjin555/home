package main

import "fmt"

var arr1 [3]int // 指定长度，然后赋值

var arr2 = [...]string{"北京", "上海", "杭州"}

var arr3 = [...]int{1: 100, 3: 500} // 指定索引位置值

var arr4 = [3][2]string{{"湖北", "武汉"}, {"浙江", "杭州"}, {"河南", "南阳"}} // 多维数组

func main() {
	fmt.Printf("数组1：%d\n", arr1)
	fmt.Printf("数组2：%s\n", arr2)
	fmt.Printf("数组3：%d\n", arr3)
	fmt.Printf("数组4：%s\n", arr4)

	fmt.Println("遍历二维数组。")
	for _, v1 := range arr4 {
		for _, v2 := range v1 {
			fmt.Printf("%s\t", v2)
		}
		fmt.Println()
	}

	// 两数之和
	/*
		var li = [...]int{1, 3, 5, 7, 8}
		target := 8
		for index1, val1 := range li {
			for index2, val2 := range li[index1:] {
				if val1+val2 == target {
					fmt.Println(index1, index1+index2)
				}
			}
		}*/

	a := [8]int{1, 2, 3, 4, 5, 6, 7, 8}
	s := a[1:3] // s := a[low:high]
	fmt.Printf("s:%v len(s):%v cap(s):%v\n", s, len(s), cap(s))
	s2 := a[3:6] // 索引的上限是cap(s)而不是len(s)
	fmt.Printf("s2:%v len(s2):%v cap(s2):%v\n", s2, len(s2), cap(s2))
}
