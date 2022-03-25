package main

type user struct {
	Id   int    `dbx:"id"`
	Age  int    `dbx:"age"`
	Name string `dbx:"name"`
}

func main() {
	//WithValueDemo()
	//RecoverDemo()
	//MysqlDemo()
	//transactionDemo() // 事务
	//sqlxDemo()    // sqlx基础CRUD
	sqlxEnhanceDemo() // sqlx事务等
	//errGroupDemo()
}
