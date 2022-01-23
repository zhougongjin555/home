package main

func fibonacci(n int, li []int) []int {
	if n < 2 {
		return li
	}
	for i := 0; i < n-2; i++ {
		new_num := li[len(li)-1] + li[len(li)-2]
		li = append(li, new_num)
	}
	return li
}

var name = "zhougongjin"

func main() {
	//var n int
	//fmt.Scan(&n)
	//var a = []int{0, 1}
	//li := fibonacci(n, a)
	//fmt.Println(li)
	//f1()
	//fmt.Println(name)

	//f4()

	pointer()
}
