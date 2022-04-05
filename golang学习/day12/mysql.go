package main

import (
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
)

// 小清单
var db *gorm.DB

func initDB() (err error) {
	dsn := "root:bt254618@tcp(127.0.0.1:3306)/website?charset=utf8mb4&parseTime=True&loc=Local"
	// 初始化全局的db
	db, err = gorm.Open(mysql.Open(dsn), &gorm.Config{})
	return err
}
