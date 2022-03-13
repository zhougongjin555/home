package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
)

func http_get(web string) {
	resp, err := http.Get(web)
	if err != nil {
		fmt.Println("无法获取网页内容")
		return
	}
	defer resp.Body.Close()
	body, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(body))
}

func getwithstr(web string) {
	data := url.Values{}
	data.Set("page", "1")
	w, err := url.ParseRequestURI(web) // 解析网址
	if err != nil {
		return
	}
	w.RawQuery = data.Encode() // 转码为url对应格式
	http_get(w.String())       // 转换为字符串
}

func http_demo() {
	getwithstr("https://liwenzhou.com")
}
