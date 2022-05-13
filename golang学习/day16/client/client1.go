// 基于RESTful API规范的数据传输方式
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

type SendParams struct {
	X float64 `json:"X"`
	Y float64 `json:"y"`
}

type RecvParams struct {
	Code int16   `json:"code"`
	Z    float64 `json:"z"`
}

func ClientDemo1() {
	url := "http://localhost:8888/square"
	params := SendParams{X: 3, Y: 4}
	paramBytes, _ := json.Marshal(params)
	resp, err := http.Post(url, "application/json", bytes.NewReader(paramBytes))
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	respBytes, _ := ioutil.ReadAll(resp.Body)
	var recv RecvParams
	json.Unmarshal(respBytes, &recv)
	fmt.Printf("接收到服务器计算的斜边长度为：%#v", recv)
}
