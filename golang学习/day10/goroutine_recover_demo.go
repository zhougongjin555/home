package main

import "fmt"

func RecoverDemo() {
	defer func() {
		if e := recover(); e != nil {
			fmt.Printf("recover panic %v\n", e)
		}
	}()

	go func() {
		defer func() {
			if e := recover(); e != nil {
				fmt.Printf("i recover a goroutine panic %v/n", e)
			}
		}()
		panic("i throw a goroutine panic")
	}()
	fmt.Println("demo close")
}
