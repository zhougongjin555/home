package main

import (
	_ "github.com/go-sql-driver/mysql"
	"github.com/jmoiron/sqlx"
	"log"
)

var dbx *sqlx.DB

func MysqlInit() error {
	// 数据库基本配置信息
	dsn := "root:bt254618@tcp(127.0.0.1:3306)/gindb?charset=utf8mb4&parseTime=True"
	var err error
	dbx, err = sqlx.Connect("mysql", dsn)
	if err != nil {
		log.Fatalf("mysql init error:%s", err)
	}
	dbx.SetMaxOpenConns(20) // 最大连接
	dbx.SetMaxIdleConns(10) // 最大空闲连接
	return nil
}
