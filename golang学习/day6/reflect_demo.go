package main

import (
	"fmt"
	"reflect"
)

type person struct { // 结构体
	name string
	age  int8
}

func (p *person) Open() {
	fmt.Println("打开...")
}

func reflectType(x interface{}) { // 空接口做函数类型，可以传入任何类型
	t := reflect.TypeOf(x)
	fmt.Printf("name(type): %v, kind: %v\n", t.Name(), t.Kind())
}

func reflectValue(x interface{}) {
	v := reflect.ValueOf(x) // 转换为反射包可读类型
	k := v.Kind()           // 获取变量的原始类型
	switch k {
	case reflect.Int64:
		// v.Int()从反射中获取整型的原始值，然后通过int64()强制类型转换
		fmt.Printf("type is int64, value is %d\n", int64(v.Int()))
	case reflect.Float32:
		// v.Float()从反射中获取浮点型的原始值，然后通过float32()强制类型转换
		fmt.Printf("type is float32, value is %f\n", float32(v.Float()))
	case reflect.Float64:
		// v.Float()从反射中获取浮点型的原始值，然后通过float64()强制类型转换
		fmt.Printf("type is float64, value is %f\n", float64(v.Float()))
	case reflect.String:
		// v.String()从反射中获取浮点型的原始值，然后通过string()强制类型转换
		fmt.Printf("type is String, value is %s\n", string(v.String()))
	default:
		fmt.Println("sorry, i don't know !!!")
	}
}

func reflectsetvalue1(x interface{}) {
	v := reflect.ValueOf(x)
	if v.Kind() == reflect.Int64 {
		v.SetInt(111)
	}
}

func reflectsetvalue2(x interface{}) {
	v := reflect.ValueOf(x)
	if v.Elem().Kind() == reflect.Int64 {
		v.Elem().SetInt(222)
	}
}

func reflect_demo() {
	// reflect.Typeof  获取基础变量类型信息
	var b bool = true
	var d int8 = 32
	fmt.Printf("%t: %v; %d: %v\n", b, reflect.TypeOf(b), d, reflect.TypeOf(d))

	// kind 获取高级封装的变量类型
	var a *float64 // 指针类型
	reflectType(a)

	type myint int8 // 自定义类型
	var mi myint = 32
	reflectType(mi)

	type mystring = string // 类型别名
	var ms mystring = "周公瑾"
	reflectType(ms)

	var p = person{"周公瑾", 54}
	reflectType(p)

	// reflect.ValueOf(x)返回的是reflect.Value类型，其中包含了原始值的值信息。reflect.Value与原始值之间可以互相转换。
	aint := 13
	var dint64 int64 = 2000000
	bfloat := 12.3456
	cstring := "周公瑾"
	reflectValue(aint)
	reflectValue(dint64)
	reflectValue(bfloat)
	reflectValue(cstring)

	// 通过反射设置变量的值
	var dat1 int64 = 25000000
	//reflectsetvalue1(dat1) // 修改的是副本，会诱发panic错误
	//fmt.Println("普通修改", dat1)
	reflectsetvalue2(&dat1)
	fmt.Println("指针修改", dat1)

}
