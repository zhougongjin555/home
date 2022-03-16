package main

import (
	"fmt"
	"net/http"
)

func getfunc(w http.ResponseWriter, r *http.Request) {
	defer r.Body.Close()
	name := r.URL.Query().Get("name")
	pwd := r.URL.Query().Get("pwd")
	fmt.Println(name, pwd)
	w.Write([]byte("200 ok"))
}

func postfunc(w http.ResponseWriter, r *http.Request) {
	defer r.Body.Close()
	name := r.PostFormValue("name")
	age := r.PostFormValue("age")
	fmt.Println(name, age)
	answer := `{"status": "200 ok"}`
	w.Write([]byte(answer))
}

func server_demo() {
	http.Handle("/get_demo", http.HandlerFunc(getfunc)) // get请求函数示例
	http.HandleFunc("/index", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("hello go world"))
	})
	http.Handle("/post_demo", http.HandlerFunc(postfunc)) // post请求函数示例
	err := http.ListenAndServe(":8003", nil)
	if err != nil {
		fmt.Println("server error")
		return
	}
}
