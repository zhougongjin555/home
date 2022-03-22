
# 并发错误处理

https://www.liwenzhou.com/posts/Go/error-in-goroutine/

## goroutine中的panic

**panic和error的区别是什么？**

error：是程序运行过程中预期可能出现的问题（错误）

panic：恐慌，是一些程序运行期间不可预期（意想不到的）的问题；代码写的有瑕疵

- 空指针
- 索引越界
- 死锁

程序遇到panic就崩掉了，可以通过recover实现平滑退出。



## errgroup
适用场景：

适合大任务拆分成多个可以并发的子任务

提供的能力：

为那些子任务的goroutine提供 sync.Wait()、error传递、基于context的取消。

![image-20220320122248942](10,连接mysql数据库.assets/image-20220320122248942.png)



g.Go(func()error)：开启一个goroutine去执行任务，只执行一次将错误赋值给`g.err`，调用一次`g.cancel`

g.Wait() : 会等待所有的子任务goroutine完成, 返回的是`g.err`



errgroup.WithContext()

看一下示例，尝试理解。



for range循环

![image-20220320124420125](10,连接mysql数据库.assets/image-20220320124420125.png)



# 操作数据库



docker快速启动一个MySQL Server容器

```bash
docker run --name mysql8019 -p 3306:13306 -d -e MYSQL_ROOT_PASSWORD=root1234 mysql:8.0.19
```



```bash
docker run -d -p 3306:3306 --name mysql  -v /opt/mysql:/var/lib/mysql -e MYSQL_DATABASE=myblog -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```



启动一个终端容器 连接上面的MySQL Server

```bash
docker run -it --network host --rm mysql:8.0.19 mysql -h127.0.0.1 -P13306 -uroot -p
```



出现这个错误就是没有导入驱动：

![image-20220320153506835](10,连接mysql数据库.assets/image-20220320153506835.png)



## sql注入

用外部输入的内容直接拼接sql导致

## sqlx

## in查询

```sql
select id, name, age from user where id in (?,?,?), (101,103,105);

insert into user (name, age) values((?,?),(?,?)) , ((jade,18), (lishuo,28))
```



## 本周作业

1. 把课上写的例子全部手敲一遍。



## 今日分享

在知道生活的真像后仍然热爱生活。









