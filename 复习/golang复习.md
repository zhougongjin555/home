# golang

## 1，why go

```bash
# go语言是为并发而诞生的语言，天生在多核的并发上更有优势，goroutine类似线程，但是并非线程，可以理解为一种虚拟线程，goroutine小号非常小（2kb），同样的内存，对于其他语言可能仅仅开辟几十上百的线程，但是对于go，可以轻松开辟他的几十上千倍goroutine。

goroutine特点：
1，可增长分段堆栈，尽在需要时开辟新的内存
2，启动比线程快
3，原生支持channel安全通讯
4，共享数据结构无需互斥锁

```

## 2，go基础相关

```go
变量声明： 简单声明，批量声明
初始化
类型推导 var name = "zhougongjin"
简短声明 age := 100

数据类型：
整型，浮点型，字符串
byte: uint8, 代表一个ascii字符
rune: int32, 代表一个utf-8字符
字符串底层[]byte，len计算的是byte长度，即一个中文长度为3

数组，切片，map
slice赋值操作都是浅拷贝，对副本赋值操作会修改所有的样本，除非使用copy函数进行深度拷贝

new用来对类型进行内存分配，会返回对应类型的空指针
make用来对slice，map，channel初始化，返回的仍然是类型自身

自定义类型： type myint int
类型别名: type byte = uint8 ; type rune = int32

结构体--
匿名结构体：var person struct{name string, age int8} 
空结构体：struct{}
内存布局，内存对齐
构造函数： 
func newPerson(name string, age int) 8person {
    return &person{name string, age int}
}
值类型接收者：深拷贝原结构体数据，对新数据修改不会影响原始副本
指针类型接收者： 方法内部的修改能够影响到原始样本

函数相关	
匿名函数：函数内部函数
函数类型与变量：type cal func(int int) int
闭包
defer: 执行在return之后，底层RET指令之前，用来释放内存，关闭连接之类
```

