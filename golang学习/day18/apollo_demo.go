package main

import (
	"fmt"
	"github.com/shima-park/agollo"
)

func ApolloDemo() {
	a, err := agollo.New(
		"localhost:8080",
		"PriceService",
		agollo.DefaultNamespace("application"),
		agollo.AutoFetchOnCacheMiss(),
		agollo.Cluster("default"),
	)
	if err != nil {
		panic(err)
	}
	fmt.Println(a.GetNameSpace("application.properties"))
	port := a.Get("apple", agollo.WithDefault("unknown"))
	fmt.Printf("get port value from apollo: %s\n", port)
}

func GetParamFromApollo(key, namespace string) (val string) {
	// apollo web端与server端接口不一致 ，注意区别
	a, err := agollo.New("localhost:8080", "PriceService", agollo.AutoFetchOnCacheMiss())
	if err != nil {
		fmt.Printf("apollo init error: %s", err)
	}

	if len(namespace) == 0 {
		namespace = "application.properties"
	}
	val = a.Get(key, agollo.WithNamespace(namespace))
	return val
}
