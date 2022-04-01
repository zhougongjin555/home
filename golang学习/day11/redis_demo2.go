/*redis使用pipeline加速的两种方式*/

package main

import (
	"context"
	"fmt"
	"github.com/go-redis/redis/v8"
	"time"
)

func redisDemo2() {
	// 使用pipeline加速redis
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	if err := redisInit(ctx); err != nil {
		fmt.Println("redis connect error: ", err)
	}

	pipe := rdb.Pipeline()
	c1 := pipe.Do(ctx, "keys", "*")                 // 操作1：获取所有的键
	c2 := pipe.MGet(ctx, "name", "age", "sex")      // 操作2：获取所有的值
	incr := pipe.Incr(ctx, "pipeline_counter")      // 操作3：设置自增键
	pipe.Expire(ctx, "pipeline_counter", time.Hour) // 操作4：为自增键设置过期时间

	_, err := pipe.Exec(ctx) // 执行管道的命令
	if err != nil {
		panic(err)
	}
	fmt.Println("all keys", c1.Val())
	fmt.Println("all values", c2.Val())
	fmt.Println(incr.Val()) // The value is available only after Exec is called.
}

// 使用pipelined就不用手动exec执行
func redisDemo3() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	if err := redisInit(ctx); err != nil {
		fmt.Println("redis connect error: ", err)
	}

	_, err := rdb.Pipelined(ctx, func(pipe redis.Pipeliner) error {
		pipe.Do(ctx, "keys", "*")                       // 操作1：获取所有的键
		pipe.MGet(ctx, "name", "age", "sex")            // 操作2：获取所有的值
		pipe.Incr(ctx, "pipeline_counter")              // 操作3：设置自增键
		pipe.Expire(ctx, "pipeline_counter", time.Hour) // 操作4：...
		return nil
	})
	if err != nil {
		panic(err)
	}

	fmt.Println("pipelined执行完成！")
}
