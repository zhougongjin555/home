package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func write_file_demo() {
	file, err := os.OpenFile("./write_file.txt", os.O_RDWR|os.O_CREATE|os.O_TRUNC, 0666)
	if err != nil {
		fmt.Println("open file failed")
		return
	}
	defer file.Close() // 再次注意，此处文件一定要有关闭操作

	// 普通方式写入文件
	dat :=
		`米奇妙妙屋
	周公瑾
	啦啦啦`
	//	str := "\n结束符号"
	//
	//	// 两种写入方式
	//	file.Write([]byte(dat)) // 以字符切片方式写入文件
	//	file.WriteString(str)   // 直接写入字符串

	// bufio 方式写入文件
	//writer := bufio.NewWriter(file)
	//i := 0
	//for { // 文件写入缓存
	//	if i == 20 {
	//		break
	//	}
	//	i++
	//	writer.WriteString("米奇妙妙屋！！！！\n")
	//}
	//writer.Flush() // 文件刷新到文件

	// ioutil 写入文件

	writer := ioutil.WriteFile("./write_file.txt", []byte(dat), 0666)
}
