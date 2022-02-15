package main

import "fmt"

func fmt_demo() {
	s1 := "周公瑾"
	fmt.Print(s1)
	fmt.Printf("%s", s1)
	fmt.Println(s1)

	n1 := 12.34
	fmt.Print(n1)
	fmt.Printf("\n%9.for i3f\n", n1) //占9位，保留三位小数
	fmt.Printf("%-9.3f\n", n1)       //占9位，保留三位小数， 右边填充空白
	fmt.Println(n1)
}
