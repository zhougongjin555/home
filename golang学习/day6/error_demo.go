package main

import "fmt"

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

func demo1() {
	fmt.Print(newError())
}
