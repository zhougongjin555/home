package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql" // mysql驱动，主要使用内部的init方法
	//_ "github.com/go-sql-driver/sqlite" // sqlite驱动
)

var db *sql.DB // 声明db对象

type user struct {
	id   int
	age  int
	name string
}

func initMysql() (err error) {
	// open 方法只是大致校验数据源字符串的格式，并没有真正的连接数据库
	db, err = sql.Open("mysql", "root:bt254618@tcp(127.0.0.1:3306)/sql_test")
	if err != nil {
		fmt.Println("database connect error")
		return err
	}
	//defer db.Close() // close方法放到 err != nil 前面，可能会导致空指针问题
	fmt.Println("init mysql success!")
	return nil
}

func queryRowDemo() {
	sqlstr := `select * from user where name = ?;`
	var u user
	err := db.QueryRow(sqlstr, "周公瑾").Scan(&u.id, &u.name, &u.age)
	if err != nil {
		fmt.Printf("scan failed, err:%v\n", err)
		return
	}
	fmt.Printf("id:%d name:%s age:%d\n", u.id, u.name, u.age)
}

func MysqlDemo() {
	if err := initMysql(); err != nil {
		fmt.Printf("init mysql failed")
		return
	}
	fmt.Println("connect success!")
	defer db.Close()
	//queryRowDemo()
}
