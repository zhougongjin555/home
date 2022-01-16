package main

import "fmt"

func f2() {
	var map1 = map[string]int{}

	map1["age1"] = 10
	map1["age2"] = 20
	fmt.Println(map1)

	//分别接受字典值，和存在状态
	v, ok := map1["age1"]
	fmt.Println(v, ok)
	type Map map[string][]int
	m := make(Map)
	s := []int{1, 2}
	s = append(s, 3)
	fmt.Printf("%+v, %p\n", s, &s[2])
	m["q1mi"] = s
	s = append(s[:1], s[2:]...)
	fmt.Printf("%+v, %p,%p\n", s, &s[0], &s[1])
	val, ok := m["q1mi"]
	fmt.Printf("%+v,%p,%p %p\n", val, &val[0], &val[1], &val[2])

}
