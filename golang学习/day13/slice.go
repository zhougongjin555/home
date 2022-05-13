package main

import "fmt"

func sliceTest() {
	a1 := []int8{1, 2, 3, 4, 5}
	a2 := a1[3:4]
	a3 := a2[:]
	fmt.Printf("a1:  %d, %d, %d, %p \n", a1, len(a1), cap(a1), &a1[0])
	fmt.Printf("a2:  %d, %d, %d, %p \n", a2, len(a2), cap(a2), &a2[0])
	fmt.Printf("a3:  %d, %d, %d, %p \n", a3, len(a3), cap(a3), &a3[0])

	// 深拷贝呢
	a4 := make([]int8, 6, 10)
	a5 := make([]int8, 6, 10)
	copy(a4, a1[3:4])
	copy(a5, a4[:])
	fmt.Printf("a1:  %d, %d, %d, %p \n", a1, len(a1), cap(a1), &a1[0])
	fmt.Printf("a4:  %d, %d, %d, %p \n", a4, len(a4), cap(a4), &a4[0])
	fmt.Printf("a5:  %d, %d, %d, %p \n", a5, len(a5), cap(a5), &a5[0])

	const i1 int8 = iota
	const i2 int8 = iota

	dic := make(map[int8]string, 6)
	dic[i1] = "zhougongjin"
	dic[i2] = "zhugeliang"
	fmt.Printf("%#v", dic)
}
