package main

import "fmt"

func namedexecDemo() {
	// 根据结构体，map插入数据
	person := make(map[string]interface{}) // 初始化键为string类型，值为空接口（任意类型）的map
	person["name"] = "wuzetian"
	person["age"] = 8
	fmt.Printf("user : %#v\n", person)

	sqlstr := `insert into user(name, age) values(:name, :age)` // :str  固定格式
	_, err := dbx.NamedExec(sqlstr, person)
	if err != nil {
		fmt.Println("sqlx namedexec error: ", err)
		return
	}
	fmt.Println("sqlx namedexec success!")
}

func sqlxEnhanceDemo() {
	if err := initDb(); err != nil {
		fmt.Println("sqlx init error: ", err)
		return
	}
	defer dbx.Close()
	namedexecDemo()
}
