package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql" // 匿名导入, mysql驱动，主要使用内部的init方法
	//_ "github.com/go-sql-driver/sqlite" // sqlite驱动
)

var db *sql.DB // 声明db对象

func initDemo() (err error) {
	// open 方法只是大致校验数据源字符串的格式，并没有真正的连接数据库
	db, err = sql.Open("mysql", "root:bt254618@tcp(127.0.0.1:3306)/test")
	if err != nil {
		fmt.Println("database connect error")
		return err
	}
	err = db.Ping() // 测试数据库是否ping通
	if err != nil {
		fmt.Println("database Ping error")
		return err
	}
	//defer db.Close() // close方法放到 err != nil 前面，可能会导致空指针问题
	fmt.Println("init mysql success!")
	return nil
}

func queryRowDemo(name string) {
	// 单行查询
	sqlstr := `select * from user where name = ?;`
	var u user
	err := db.QueryRow(sqlstr, name).Scan(&u.Id, &u.Name, &u.Age)
	if err != nil {
		fmt.Printf("scan failed, err:%v\n", err)
		return
	}
	fmt.Printf("get data: %#v\n", u)
}

func queryDemo() {
	// 多行查询
	sqlstr := `select * from user`
	rets, err := db.Query(sqlstr)
	if err != nil {
		fmt.Println("database query error")
		return
	}

	// 循环读取结果集中的数据
	for rets.Next() {
		var u user
		err = rets.Scan(&u.Id, &u.Name, &u.Age)
		if err != nil {
			fmt.Println("data scan error")
		}
		fmt.Printf("get datas: %#v\n", u)
	}
}

func execDemo(option string) {
	var sqlstr string // 先声明变量，不然再switch里面声明，变量无法传递到switch代码块外部
	switch option {
	case "insert":
		sqlstr = `insert into user(name, age) values("zhaozilong", "28")`
	case "update":
		sqlstr = `update user set name="zhangyide" where id = 5`
	case "delete":
		sqlstr = `delete from user where id = 5`
	default:
		sqlstr = ``
	}
	ret, err := db.Exec(sqlstr)
	if err != nil {
		fmt.Println("database exec error")
		return
	}
	n, _ := ret.RowsAffected() // 获取收到影响的行数
	fmt.Println("affected rows: ", n)
}

func MysqlDemo() {
	if err := initDemo(); err != nil {
		fmt.Printf("init mysql failed")
		return
	}
	fmt.Println("connect success!")
	defer db.Close()
	//queryRowDemo("zhougongjin")
	//queryDemo()
	execDemo("insert")
}
