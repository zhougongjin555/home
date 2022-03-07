package main

import (
	"fmt"
	"strconv"
	"sync"
)

//var dic = map[string]int
//func set(key string, val int) {
//	dic.LoadOrStore(key)
//	dic[key] = val
//}
//
//func get(key string) int {
//	return dic[key]
//}
var dic = sync.Map{}

func sync_map_demo() {
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func(n int) {
			key := strconv.Itoa(n)
			dic.Store(key, n)
			val, _ := dic.Load(key)
			fmt.Printf("key: %s, value: %d\n", key, val)
			wg.Done()
		}(i)
	}
}
