package main

import (
	"errors"
	"fmt"
)

type MySQLError struct {
	Code int8
	Msg  string
}

func (m *MySQLError) Error() string {
	return m.Msg
}

func queryDB() error {
	var err = &MySQLError{8, "数据库出错"}
	return err
}

func newError() error {
	err := queryDB()
	newerr := fmt.Errorf("%w才怪, 我骗你的", err)
	return newerr
}

func error_demo() {
	var EOF = errors.New("EOF")
	fmt.Println(EOF)

	// %v 普通包装
	newerr := fmt.Errorf("包装后的错误(不保留原错误类型)：%v", EOF)
	fmt.Println(newerr)

	// %w 深层包装
	package_err := fmt.Errorf("保留原类型并重新包装的错误类型: %w", EOF)
	fmt.Println(package_err)

	fmt.Println("判断前面错误类型是否包含后面的", errors.Is(package_err, EOF))
	fmt.Println("解包错误类型", errors.Unwrap(package_err))
	//fmt.Print(newError())
}
