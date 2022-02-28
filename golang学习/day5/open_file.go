package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

func open_file_demo() {
	file, err := os.Open("./open_file.txt") // 默认只读方式打开文件
	if err != nil {
		fmt.Println("open file failed, err", err)
		return
	}
	defer file.Close() // 配合os.Open(...) 捕获错误

	/*// 1，循环读取文件
	var content []byte
	var tmp = make([]byte, 1024) // 每次读取的大小，必须为byte类型的切片
	for {
		n, err := file.Read(tmp) // 会返回读取的字节数以及具体报错信息，读取到文件末尾会返回“ 0 ”和“ io.EOF ”
		if err == io.EOF {
			fmt.Println("文件为空")
			break
		}
		if err != nil {
			fmt.Printf("read file error, err:", err)
			return
		}
		content = append(content, tmp[:n]...)
	}
	//fmt.Println(string(content))  // 读取的文件类型为byte类型，使用string(**)可以转换为可读类型
	fmt.Println(string(tmp))
	*/

	// 2, bufio 包读取文件
	//reader := bufio.NewReader(file)
	//for {
	//	line, err := reader.ReadString('\n') // 每次读取的截至符号，用单引号表示为字符
	//	if err == io.EOF {
	//		if len(line) != 0 {
	//			fmt.Print(line)
	//		}
	//		fmt.Println("\n文件读取完成")
	//		break
	//	}
	//	if err != nil {
	//		fmt.Printf("read file error, err:", err)
	//		return
	//	}
	//	fmt.Print(line)
	//}

	// ioutil 方式读取文件
	content, err := ioutil.ReadFile("open_file.txt")
	if err != nil {
		fmt.Println("read file error")
		return
	}
	fmt.Printf("%s", content)
}
