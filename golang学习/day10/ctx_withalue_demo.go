package main

import (
	"context"
	"fmt"
)

type CtxKey int8

const (
	CtxName CtxKey = iota
	CtxAge  CtxKey = iota
	// ...
)

func WithValueDemo() {
	ctx := context.WithValue(context.Background(), CtxName, "周公瑾")

	// 根据key取值
	value := ctx.Value(CtxName).(string) // 对取出的值做类型断言
	fmt.Printf("key: %#v, value: %#v", CtxName, value)

}
