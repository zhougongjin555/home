/*redis初始化、redis基础操作*/

package main

import (
	"context"
	"fmt"
	"github.com/go-redis/redis/v8"
	"time"
)

var rdb *redis.Client

func redisInit(ctx context.Context) (err error) {
	rdb = redis.NewClient(&redis.Options{
		Addr:       "127.0.0.1:6379",
		DB:         0,   // 使用默认的redis库
		MaxRetries: 3,   // 重连的最大次数
		PoolSize:   100, // 设置连接池大小
	})
	//time.Sleep(time.Second * 3)
	_, err = rdb.Ping(ctx).Result()

	if err != nil {
		fmt.Println("redis init error : ", err)
		return err
	}
	fmt.Println("redis connect successful")
	return nil
}

func redisSetDemo(ctx context.Context) {
	// 设置键值
	err := rdb.Set(ctx, "age", 18, 0) // 最后参数为过期时间，0为不过期
	if err != nil {
		fmt.Println("redis init error : ", err)
		return
	}
}

func redisGetDemo(ctx context.Context) {
	// 取出键值
	val, err := rdb.Get(ctx, "name").Result()
	switch {
	case err == redis.Nil: // 用来区分空字符串和空key
		fmt.Println("key does not exist")
	case err != nil:
		fmt.Println("Get failed", err)
	case val == "":
		fmt.Println("value is empty")
	}
	fmt.Println("get date from redis:", val)

}

func redisDoDemo(ctx context.Context) {
	val, err := rdb.Do(ctx, "get", "age").Result()
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(val)

}

func redisDemo1() {
	// 传递context，设置redis连接过期时间
	ctx, cancel := context.WithTimeout(context.Background(), time.Second*2)
	defer cancel()
	if err := redisInit(ctx); err != nil {
		fmt.Println("redis connect error: ", err)
	}

	//redisSetDemo(ctx)
	//redisGetDemo(ctx)
	//redisDoDemo(ctx)
}
