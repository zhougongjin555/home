package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"go.uber.org/zap"
)

type Book struct {
	// 传递指针的好处
	// 当字段required时，可以避免由于前端传递字段零值时候被gin框架误认为未传递字段
	ID        int     `json:"-"`
	Title     *string `form:"title" json:"title" binding:"required"`
	Author    *string `form:"author" json:"author" binding:"required"`
	Publisher *string `form:"publisher" json:"publisher" binding:"required"`
}

func createBookHandler(c *gin.Context) {
	// 接收前端返回参数--放到数据库
	var book Book
	if err := c.ShouldBind(&book); err != nil {
		logger.Error("need book params!!",
			zap.Error(err))
		c.JSON(200, gin.H{
			"code": 999,
			"msg":  "your params is not completed",
		})
		return
	}

	// 插入数据导数据库
	sqlStr := "insert into book (title, author, publisher) values (:title, :author, :publisher)"
	ret, err := dbx.NamedExec(sqlStr, book)
	if err != nil {
		logger.Error("insert sql error!!", zap.Error(err))
	}
	id, _ := ret.LastInsertId()
	n, _ := ret.RowsAffected()

	// 返回响应
	c.JSON(200, gin.H{
		"code":   0,
		"msg":    "success",
		"data":   book,
		"id":     id,
		"affect": n,
	})
	logger.Info("create a new book!!")
}

func deleteBookHandler(c *gin.Context) {

}

func updateBookHandler(c *gin.Context) {

}

func getBookHandler(c *gin.Context) {
	var book Book
	var books []string
	sqlx := "select title, author, publisher from book;"
	rows, err := dbx.NamedQuery(sqlx, book)
	if err != nil {
		logger.Error("get sqlx error", zap.Error(err))
	}
	defer rows.Close()

	// 遍历取出数据
	for rows.Next() {
		_ = rows.StructScan(&book)
		b := fmt.Sprintf("book{title: %s, author: %s, publisher: %s}", *(book.Title), *(book.Author), *(book.Publisher))
		books = append(books, b)
	}

	c.JSON(200, gin.H{
		"code": 0,
		"msg":  "success",
		"book": books,
	})
	logger.Info("someone get books!!")
	//sugerlogger.Infof("sugerlogger: someone get books!!!")
}
