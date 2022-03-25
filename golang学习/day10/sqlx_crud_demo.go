package main

import (
	"fmt"
	"github.com/jmoiron/sqlx"
)

var dbx *sqlx.DB

func initDb() (err error) {
	dsn := "root:bt254618@tcp(127.0.0.1:3306)/test"
	dbx, err = sqlx.Connect("mysql", dsn)
	if err != nil {
		fmt.Println("database init error", err)
		return err
	}
	fmt.Println("database init success!")
	return nil
}

func queryRowDB(name string) {
	// 单行查询
	sqlstr := `select * from user where name = ?`
	var u user
	err := dbx.Get(&u, sqlstr, name)
	if err != nil {
		fmt.Println("dbx get error: ", err)
		return
	}
	fmt.Printf("sqlx get data: %#v\n", u)
}

func queryDB() {
	// 多行查询
	sqlstr := `select * from user`
	var users []user
	err := dbx.Select(&users, sqlstr)
	if err != nil {
		fmt.Println("dbx select error: ", err)
		return
	}
	fmt.Printf("sqlx get datas: %#v\n", users)
}

func execDb(option string) {
	var sqlstr string // 先声明变量，不然再switch里面声明，变量无法传递到switch代码块外部
	switch option {
	case "insert":
		sqlstr = `insert into user(name, age) values("zhaozilong", "28")`
	case "update":
		sqlstr = `update user set name="zhangyide" where name = "zhaozilong"`
	case "delete":
		sqlstr = `delete from user where name = "zhangyide"`
	default:
		sqlstr = ``
	}
	ret, err := dbx.Exec(sqlstr)
	if err != nil {
		fmt.Println("database exec error")
		return
	}
	n, _ := ret.RowsAffected() // 获取收到影响的行数
	fmt.Println("affected rows: ", n)
}

func sqlxDemo() {
	if err := initDb(); err != nil {
		return
	}
	defer dbx.Close()
	queryRowDB("zhougongjin")
	queryDB()
	execDb("delete")
}
