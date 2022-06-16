package main

import (
	"fmt"
	"github.com/hashicorp/consul/api"
	"net"
	"strconv"
)

type consul struct {
	client *api.Client
}

// 连接consul
func NewConsul(addr string) (*consul, error) {
	cfg := api.DefaultConfig()
	cfg.Address = addr
	c, err := api.NewClient(cfg)
	if err != nil {
		return nil, err
	}
	return &consul{c}, nil
}

// 将服务注册到consul
func (c *consul) RegisterService(serviceID, IP string) error {
	res := GetParamFromApollo("port", "")
	port, _ := strconv.Atoi(res)
	ip, _ := GetMyIp() // 获取本机IP地址
	// 健康检测相关配置
	check := &api.AgentServiceCheck{
		GRPC:                           fmt.Sprintf("%s:%s", ip, res),
		Timeout:                        "10s", // 超时
		Interval:                       "10s", // 监测间隔
		DeregisterCriticalServiceAfter: "20s", // 超时注销服务
	}

	// 注册相关配置
	srv := &api.AgentServiceRegistration{
		ID:      serviceID,
		Name:    "get_fruit_price_service",
		Tags:    []string{"周公瑾"},
		Address: IP,
		Port:    port,
		Check:   check,
	}
	return c.client.Agent().ServiceRegister(srv)
}

func (c *consul) DeregisterService(serviceID string) error {
	return c.client.Agent().ServiceDeregister(serviceID)
}

// 获取本机IP地址
func GetMyIp() (net.IP, error) {
	conn, err := net.Dial("udp", "8.8.8.8:80")
	if err != nil {
		return nil, err
	}
	defer conn.Close()
	localAddr := conn.LocalAddr().(*net.UDPAddr)
	return localAddr.IP, nil
}
