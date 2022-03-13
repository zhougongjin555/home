package main

import (
	"fmt"
	"net/http"
)

func f1(w http.ResponseWriter, r *http.Request) {
	//fmt.Println("hello world  -- from go")

	id := r.URL.Query().Get("id") // 获取url中的参数

	w.Write([]byte("hello world  -- from go   = " + id))
}

func server_demo() {
	http.Handle("/index", http.HandlerFunc(f1))
	err := http.ListenAndServe(":8003", nil)
	if err != nil {
		fmt.Println("server error")
		return
	}
}
