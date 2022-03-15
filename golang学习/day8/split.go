package main

import "strings"

func split(s, str string) (result []string) { // result 已经声明，所以先买你的函数中无需再次声明
	index := strings.Index(s, str)
	if index == -1 {
		return
	} else {

	}

}

func demo2() {
	split("周公瑾爱舟舟", "公")
}
