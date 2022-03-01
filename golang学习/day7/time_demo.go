package main

import (
	"fmt"
	"time"
)

func time_demo() {
	now := time.Now()
	fmt.Println(now)

	t := time.Date(2022, 02, 22, 22, 22, 22, 22, time.Local)
	var (
		sec  = t.Unix()      // 秒
		msec = t.UnixMilli() // 毫秒
		nsec = t.UnixMicro() // 微秒
	)
	fmt.Println(sec, msec, nsec)

	// 将秒级时间戳转为时间对象（第二个参数为不足1秒的纳秒数）
	timeObj := time.Unix(sec, 22)
	fmt.Println(timeObj)           // 2022-02-22 22:22:22.000000022 +0800 CST
	timeObj = time.UnixMilli(msec) // 毫秒级时间戳转为时间对象
	fmt.Println(timeObj)           // 2022-02-22 22:22:22 +0800 CST
	timeObj = time.UnixMicro(nsec) // 微秒级时间戳转为时间对象
	fmt.Println(timeObj)           // 2022-02-22 22:22:22 +0800 CST

	// 时间的加减，判断时间的大小相等
	one_later := now.Add(time.Hour * time.Duration(10)) // 倍数相乘需要转换位During类型
	fmt.Println("一小时后", one_later)
	two_before := now.Sub(t) // 比较两个时间的差值
	fmt.Println("时间之差", two_before)
	fmt.Printf("%#v 时间相等   %#v?   %t\n", now, t, now.Equal(t))
	fmt.Printf("大于？%t，，，小于？%t", now.Before(t), now.After(t))

	// Tick定时器
	//ticker := time.Tick(time.Duration(2) * time.Second)
	//for i := range ticker {
	//	fmt.Println("2s了， 我该打印了:", i)
	//}

	// Time类型格式化
	fmt.Println(now.Format("2006-01-02 15:04:05.999")) // 999 省略末尾的0//0000，表示四位小数
	fmt.Println(now.Format("01/02-2006, 04:05.0000"))

	// 解析字符串类型的时间
	time4, err := time.Parse(time.RFC3339, "2022-10-05T11:25:20+08:00")
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println("解析后的时间", time4) // 2022-10-05 11:25:20 +0800 CST
}
