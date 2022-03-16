package main

import (
	"context"
	"fmt"
	"time"
)

func with_demo() {

	// WithDeadline
	d := time.Now().Add(time.Second)
	ctx, cancel := context.WithDeadline(context.Background(), d)
	defer cancel()
	select {
	case <-time.After(time.Second * 3): // 等待3s
		fmt.Println("已经经过1s")
	case <-ctx.Done(): // 从context获取结束信号
		fmt.Println("任务结束, 结束原因：%s", ctx.Err()) // ctx.Err()存储结束信息
	}

}
