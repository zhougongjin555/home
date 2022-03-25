package main

import (
	"fmt"
	"golang.org/x/sync/errgroup"
	"net/http"
)

func errGroupDemo() error {
	g := new(errgroup.Group)
	var urls = []string{
		"https://baidu,com",
		"https://taobao.com",
		"https://zhouzhou123.com",
	}

	for _, url := range urls {
		g.Go(func() error {
			res, err := http.Get(url)
			if err == nil {
				fmt.Printf("%s connect success\n", url)
				res.Body.Close() // 及时关闭url通道
			}
			return err
		})
	}

	if err := g.Wait(); err != nil {
		fmt.Println(err)
		return err
	}
	return nil
}
