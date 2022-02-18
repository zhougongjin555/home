package main

import "fmt"

type Payer interface {
	Pay(float64)
}

// 定一两个支付结构体
type AliPay struct {
}
type WechatPay struct {
}

// 为结构体实现接口方法
func (a *AliPay) Pay(amount float64) { // 指针接收者实现接口
	fmt.Printf("支付宝支付: %.2f\n", amount)
}
func (w WechatPay) Pay(amount float64) { // 值接收者实现接口
	fmt.Printf("微信支付: %.2f\n", amount)
}

// 实现方法调用
func Payment(p Payer, amount float64) {
	p.Pay(amount)
}

func demo() {
	var a1 *AliPay // 指针接收者只能接收指针类型的变量来传入方法
	Payment(a1, 2222.2222)

	var w1 WechatPay // 值接收者只能接受值类型的变量来传入方法
	Payment(w1, 300.22)

	// 测试值类型和指针类型的结构体，能否赋值给接口
	var pa1, pa2, pw1, pw2 Payer

	//var a2 = AliPay{}  // 指针类型的结构体不能使用值类型初始化赋值给接口
	var a3 = &AliPay{}
	//pa1 = a2
	pa2 = a3
	pa1.Pay(22.22)
	pa2.Pay(22.22)

	var w2 = WechatPay{}
	var w3 = &WechatPay{} // 值类型结构体可以使用指针类型初始化并赋值给接口
	pw1 = w2
	pw2 = w3
	pw1.Pay(22.22)
	pw2.Pay(22.22)
}
