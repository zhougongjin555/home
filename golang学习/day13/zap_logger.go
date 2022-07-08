package main

import (
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
	"os"
)

var logger *zap.Logger
var sugerlogger *zap.SugaredLogger

func InitLogger() {
	//	logger, _ = zap.NewProduction()
	//	//logger, _ = zap.NewDevelopment()
	//	//logger = zap.NewExample()
	sugerlogger = logger.Sugar()
}

// 自定义logger
func getEncoder() zapcore.Encoder {
	encoderConfig := zap.NewProductionEncoderConfig()
	encoderConfig.EncodeTime = zapcore.ISO8601TimeEncoder   // 修改日志中时间编码的格式
	encoderConfig.EncodeLevel = zapcore.CapitalLevelEncoder // 使用大写字母表示日志级别
	return zapcore.NewJSONEncoder(encoderConfig)
}

func getLogWriter() zapcore.WriteSyncer {
	file, _ := os.Create("./test.log")
	return zapcore.AddSync(file)
}

func InitMyLogger() {
	writeSyncer := getLogWriter()
	encoder := getEncoder()
	core := zapcore.NewCore(encoder, writeSyncer, zapcore.DebugLevel)

	logger = zap.New(core, zap.AddCaller()) // addcaller 用来再日志中显示调用函数信息
}
