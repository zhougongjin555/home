/*redis事务，watch*/

package main

import (
	"context"
	"fmt"
	"github.com/go-redis/redis/v8"
	"time"
)

func redisTransactionsDemo() {
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	if err := redisInit(ctx); err != nil {
		fmt.Println("redis init failed", err)
	}

	options := func(pipe redis.Pipeliner) error {
		c1 := rdb.Get(ctx, "name")
		c2 := rdb.Get(ctx, "sex")
		fmt.Println(c1.Val(), c2.Val())
		return nil
	}
	_, err := rdb.TxPipelined(ctx, options)
	if err != nil {
		panic(err)
	}
	fmt.Println("事务执行完成")
}

func watchDemo(key string) {
	err := rdb.Watch(context.Background(), func(tx *redis.Tx) error {
		// pipe := tx.TxPipeline()
		// pipe.Set(context.Background(), key, 100, time.Hour)
		// time.Sleep(5 * time.Second) // 假设操作比较耗时
		// _, err := pipe.Exec(context.Background())
		// return err
		_, err := tx.TxPipelined(context.Background(), func(pipe redis.Pipeliner) error {
			pipe.Set(context.Background(), key, 100, time.Hour)
			time.Sleep(5 * time.Second) // 假设操作比较耗时
			_, err := pipe.Exec(context.Background())
			return err
		})
		return err
	}, key)

	fmt.Println(err)
	fmt.Println(rdb.Get(context.Background(), key).Int())
}
