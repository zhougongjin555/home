package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
)

func client_demo() {
	web := "https://localhost:8004"
	data := url.Values{"name": {"zhougongjin"}, "pwd": {"zhouzhou123"}}
	web = web + "?" + data.Encode()
	resp, err := http.Get(web)
	defer resp.Body.Close()
	if err != nil {
		fmt.Println("http get errors")
		return
	}
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("read body error")
		return
	}
	fmt.Println(string(body))
	data.Encode()
}
