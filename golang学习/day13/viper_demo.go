package main

import (
	"fmt"
	"github.com/fsnotify/fsnotify"
	"github.com/spf13/viper"
)

func SetValue() {
	// viper配置参数
	viper.SetDefault("name", "周公瑾")
	viper.AddConfigPath("./conf")
	viper.SetConfigType("toml")
	viper.SetConfigName("demo")
	if err := viper.ReadInConfig(); err != nil {
		if _, ok := err.(viper.ConfigFileNotFoundError); ok {
			logger.Error("config file not found")
		} else {
			logger.Error("there are some other wrongs!!")
		}
	}
}

func ReadValue() {
	// viper读取参数信息
	viper.WatchConfig()
	viper.OnConfigChange(func(e fsnotify.Event) {
		fmt.Println("config changed: ", e.Name)
	})
}

func ViperDemo() {
	SetValue()
	ReadValue()
	fmt.Println("viper get conf from file: ", viper.Get("type.str1"))
}
