

# 基于centos7 + Nginx + python + Django + uwsgi + mysql 部署的WEB项目

## 0，基础环境配置

```
# 一些特定的依赖环境
yum install gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel -y
```



## 1，python3安装

- 下载python源码

  ```
  // yum install wget -y 
  
  wget  https://www.python.org/ftp/python/3.8.9/Python-3.8.9.tgz 
  ```



- 解压缩源码文件并进入目录

  ```
  tar -zxvf Python-3.8.9.tgz //解压缩
  
  cd Python-3.8.9        //进入目录
  ```

  

- 编译三部曲

  ```
  ./configure --prefix=/opt/python389/         // ='...安装路径...'
  
  make && make install                         // 编译安装
  ```



- 配置环境变量

  ```
  vim /etc/profile                             // 进入vim编辑器
  
  PATH="/opt/python389/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:"      // 再最前面加入执行文件路径
  
  source /etc/profile
  ```



`删除软件`： 1，删除软件目录     2，删除PATH里面的路径



## 2，virtualenv安装使用

```
1, 安装库
	pip3 instll -i https://pypi.douban.com/simple virtualenv

2，创建虚拟环境
	virtualenv --python=python3 venv1
	
3，激活虚拟环境
	source /opt/venv1/bin/activate           // 后面路径为虚拟环境创建位置

4，退出虚拟环境
	deactivate								 // 直接执行此命令，退出虚拟环境，系统会自动删除venv的PATH，也就表示退出了

```







## 3，uwsgi安装使用

```
1，安装库
	pip3 install -i https://pypi.douban.com/simple uwsgi
	
2，在项目（django）根目录里面配置uwsgi.ini文件
	touch uwsgi.ini
	vim uwsgi.ini
	

[uwsgi]
uid = root
gid = root

# 指定项目文件的地址
chdir           = /opt/tf_crm/
module          = tf_crm.wsgi
home            = /opt/tf_crm/venv_crm


socket = 127.0.0.1:8000
#  http =  0.0.0.0:8000

master = true //启动主进程
# 代表定义uwsgi运行的多进程数量，官网给出的优化建议是 2*cpu核数+1
# processes       = 3
vhost = true //多站模式
no-site = true //多站模式时不设置⼊⼝模块和⽂件
workers = 2 //⼦进程数
reload-mercy = 10 //平滑的重启
vacuum = true //退出、重启时清理⽂件
max-requests = 1000 //开启10000个进程后, ⾃动respawn下
limit-as = 512 // 将进程的总内存量控制在512M 
buffer-size = 30000
pidfile = /var/run/uwsgi9090.pid //pid⽂件，⽤于下⾯的脚本启动、停⽌该进程
daemonize = /website/uwsgi9090.log  //日志文件




3，启动uwsgi服务
	uwsgi --ini ./uwsgi.ini

4，关闭uwsgi
	ps -ef | grep 'uwsgi'   # 找到uwsgi的进程pid
    kill -9 pid     # 根据上面的pid杀死进程即可
    netstat -ntpl     # 检查进程是否已经关闭
```





## 4，mysql安装使用

```
# 缺点：超过1500w行数据之后可能出现瓶颈


[root@localhost src]# yum  install mariadb-server           安装mariadb数据库
[root@localhost src]# yum  clean   all                 清空已安装文件   如果下载失败之后执行的.

[root@localhost src]# mysql_secure_installation # 数据库初始化（重设密码）


1.   启动命令    [root@localhost src]# systemctl  start  mariadb
2.   重启命令    [root@localhost src]# systemctl  restart  mariadb
3.   关闭命令    [root@localhost src]# systemctl  stop  mariadb
4.   设定开机自起 [root@localhost src]# systemctl  enable mariadb 
5.   关闭开机自起 [root@localhost src]# systemctl  disable mariadb 

```







## 5，nginx安装使用

- 配置基础环境

```
  yum install gcc patch libffi-devel python-devel  zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel openssl openssl-devel -y
```



- 下载nginx源码并解压缩

```
  wget http://tengine.taobao.org/download/tengine-2.3.3.tar.gz
  
  tar -zxvf tengine-2.3.3.tar.gz
```



- 编译三部曲

```
  ./configure --prefix=/opt/tngx233/
  make && make install 
```

  

- 修改环境变量

```
  vim /etc/profile
  PATH="/opt/tngx232/sbin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:"
```

  

- 启动nginx

```
  首次启动nginx，注意要关闭防火墙
  直接输入nginx命令即可启动
  有关nginx的命令
  
  nginx						 #首次输入是直接启动，不得再次输入 
  nginx -s reload  #平滑重启，重新读取nginx的配置文件，而不重启进程
  nginx -s stop  	#停止nginx进程 
  nginx -t   #检测nginx.conf语法是否正确
  
  默认访问nginx的首页站点url是
  http://192.168.178.140:80/index.html
  
```

  

- 配置nginx配置文件

```
server { 
 	listen 80;
 	server_name localhost;
 	#access_log logs/abc.log main;
    location / {
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:9090;  # 指定端口
        uwsgi_param UWSGI_SCRIPT baism_web.wsgi;   # 对应到项目文件里面的wsgi.py文件
        uwsgi_param UWSGI_CHDIR /usr/local/nginx/html/baism_web;   # 对应到项目的首级目录即可
        index index.html index.htm;
        client_max_body_size 35m;
        #uwsgi_cache_valid 1m;
        #uwsgi_temp_file_write_size 64k;
        #uwsgi_busy_buffers_size 64k;
        #uwsgi_buffers 8 64k;
        #uwsgi_buffer_size 64k;
        #uwsgi_read_timeout 300;
        #uwsgi_send_timeout 300;
        #uwsgi_connect_timeout 300;
	}
}

```



# 其他软件

## 0，更换yum源

yum源的默认仓库文件夹是 `/etc/yum.repos.d/`，只有在这个目录`第一层`的*.repo结尾的文件，才会被yum读取

```
1.下载wget命令
yum install wget -y   #wget命令就是在线下载一个url的静态资源

2.备份旧的yum仓库源
cd  /etc/yum.repos.d

mkdir  repobak
mv *.repo   repobak  #备份repo文件

3.下载新的阿里的yum源仓库，阿里的开源镜像站https://developer.aliyun.com/mirror/
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

4.继续下载第二个仓库 epel仓库
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo

5.此时已经配置完毕，2个新的yum仓库，可以自由的嗨皮，下载软件了
[root@s25linux yum.repos.d]# ls
CentOS-Base.repo  epel.repo  repobak

6.下载一个redis玩一玩
[root@s25linux yum.repos.d]# yum install redis -y  #就能够自动的下载redis，且安装redis

7.此时可以启动redis软件了，通过yum安装的redis，这么启动
systemctl  start redis   

8.使用redis的客户端命令，连接redis数据库
[root@s25linux yum.repos.d]# redis-cli

127.0.0.1:6379> ping
PONG




```

## 1，supervisor安装使用

```
1，安装工具
	yum install supervisor -y
	
2，生成配置文件
	echo_supervisord_conf >  /etc/supervisord.conf
	
3，修改配置文件
	vim /etc/supervisord.conf

	[program:zhougongjin]       
    command=写入启动uwsgi的命令  ;supervisor其实就是在帮你执行命令而已！
    autostart=true       ; 在supervisord启动的时候也自动启动
    startsecs=10         ; 启动10秒后没有异常退出，就表示进程正常启动了，默认为1秒
    autorestart=true     ; 程序退出后自动重启,可选值：[unexpected,true,false]，默认为unexpected，表示进程意外杀死后才重启
    stopasgroup=true     ;默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
    killasgroup=true     ;默认为false，向进程组发送kill信号，包括子进程

4，启动supervisor
	supervisord -c /etc/supervisord.conf
```

## 2，redis配置

- 安全配置

  ```
  vim /etc/redis.conf
  
  # 换绑定ip，端口，设置密码，开启安全模式，后台运行
  
  bind 0.0.0.0
  port 6500
  requirepass bt254618
  protected-mode yes
  daemonize yes
  
  
  # 按照配置文件启动redis
  redis-server /etc/redis.conf
  redis-cli -h 0.0.0.0 -p 6500
  ```

  

- 数据持久化

  - RDB机制

  ```
  # 配置文件在上面的基础上加上几行
  # 分别代表：指定运行日志文件，指定数据文件存放路径，指定数据持久化文件名称
  
  
  logfile /data/6500/redis.log
  dir /data/6500
  dbfilename zhougongjin.rdb
  save 900 1
  save 300 10
  save 60 10000
  
  ```

  - AOF机制

  ```
  # 配置文件在上面的基础上加上几行
  # 分别代表：指定运行日志文件，指定数据文件存放路径，开启aof机制，每秒持久化一次
  
  logfile /data/6500/redis.log
  dir /data/6500
  appendonly yes
  appendsunc everysec   
  ```

  

- 数据主从关系配置/同步复制

  ```
  # 准备两个配置文件，主配置文件不做修改，从配置文件加上一行slaveof (host) (port)
  
  # 配置1(主)
  bind 0.0.0.0
  port 6500
  requirepass bt254618
  protected-mode yes
  daemonize yes
  pidfile /data/6500/redis.pid
  loglevel notice
  logfile /data/6500/redis.log
  dir /data/6500
  appendonly yes
  appendsunc everysec
  protected-mode no
  
  # 配置2(从)
  bind 0.0.0.0
  port 6600
  requirepass bt254618
  protected-mode yes
  daemonize yes
  pidfile /data/6500/redis.pid
  loglevel notice
  logfile /data/6500/redis.log
  dir /data/6500
  appendonly yes
  appendsunc everysec
  protected-mode no
  slaveof 0.0.0.0 6600
  
  
  # 查看redis信息
  redis-cli -p 6500 info replication
  ```

  

- redis哨兵

  ```
  # 一般是准备3个哨兵，投票决定主库挂掉之后哪个库当主库
  # 配置三个哨兵文件，除了端口号，其他相同
  
  
  # 哨兵配置1   s25-sentinel-26380.conf 
  port 26380
  dir /var/redis/data/
  logfile "26380.log"
  sentinel monitor s25msredis 127.0.0.1 6379 2
  sentinel down-after-milliseconds s25msredis 30000
  sentinel parallel-syncs s25msredis 1
  sentinel failover-timeout s25msredis 180000
  daemonize yes
  
  
  # 哨兵配置2    s25-sentinel-26381.conf 
  port 26381
  dir /var/redis/data/
  logfile "26380.log"
  sentinel monitor s25msredis 127.0.0.1 6379 2
  sentinel down-after-milliseconds s25msredis 30000
  sentinel parallel-syncs s25msredis 1
  sentinel failover-timeout s25msredis 180000
  daemonize yes
  
  
  # 哨兵配置3    s25-sentinel-26382.conf 
  port 26382
  dir /var/redis/data/
  logfile "26380.log"
  sentinel monitor s25msredis 127.0.0.1 6379 2
  sentinel down-after-milliseconds s25msredis 30000
  sentinel parallel-syncs s25msredis 1
  sentinel failover-timeout s25msredis 180000
  daemonize yes
  
  
  # 启动哨兵
  redis-sentinel s25-sentinel-26380.conf 
  redis-sentinel s25-sentinel-26381.conf 
  redis-sentinel s25-sentinel-26382.conf 
  
  
  ```

  

- redis-cluster搭建

  ```
  # 最少配置6个redis-cluster节点，区别仅在端口不同
  
  # 配置1-6    s25-redis-7000.conf/s25-redis-7001.conf/....     仅port不同
  port 7000
  daemonize yes
  dir "/opt/redis/data"
  logfile "7000.log"
  dbfilename "dump-7000.rdb"
  cluster-enabled yes   #开启集群模式
  cluster-config-file nodes-7000.conf　　#集群内部的配置文件
  cluster-require-full-coverage no　　#redis cluster需要16384个slot都正常的时候才能对外提供服务，换句话说，只要任何一个slot异常那么整个 										cluster不对外提供服务。 因此生产环境一般为no
  
  # 按照启动redis的方法启动集群
  redis-server s25-redis-7000.conf
  redis-server s25-redis-7001.conf
  ....
  
  到此位置，还不能写入数据...
  -------------------------------------------------------------
  
  # 下载ruby
  yum install ruby -y
  
  # 下载ruby操作redis的模块
  wget http://rubygems.org/downloads/redis-6.2.5.gem
  
  # gem（相当于py的pip）安装上面的模块
  gem install redis-6.2.5.gem
  
  # 搜索ruby创建的redis集群脚本
  find / -name "redis-trib.rb" 
  
  # 创建集群
  redis-trib.rb create --replicas 1 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005
  
  ```

## 3，docker

- docker安装

  ```
  # 参考官方文献
  
  https://docs.docker.com/engine/install/centos/
  
  ```

  

- 

  ```
  1.创建docker镜像
  docker pull ubuntu
  
  2.搜索docker镜像
  docker search ubuntu
  
  3.运行docker镜像（如果镜像不存在，会自动下载）
  docker run ubuntu
  	
  	交互式的运行一个存活的docker容器，centos
  	# -i 是交互式的命令操作   -t开启一个终端   /bin/bash 指定shell解释器
  	# -d 后台运行   -d 指定一段shell代码
  	# --name 指定容器的名字
  	# 容器空间内，有自己的文件系统 
  	docker run -it  centos  /bin/bash 	#运行centos镜像，且进入容器内
  
  4.查看本地机器，所有的镜像文件内容
  docker  images 
  
  5.删除镜像
  docker rmi 镜像id
  
  6.查看docker正在运行的进程
  docker ps 
  docker ps -a    # 查看所有运行，以及挂掉的容器进程
  
  7.查看容器内的运行日志
  docker logs  容器id
  docker logs -f  容器id   #实时刷新容器内的日志，例如检测nginx等日志信息
  
  8.查看容器内的端口转发情况
  docker port  容器id  #查看容器的端口转发
  
  9.删除容器记录
  docker rm 容器id
  	# 批量删除无用的容器记录
  	docker rm `docker ps -aq`
  	
  10.进入容器控件内，修改内部资料
  docker exec --it 容器id  /bin/bash
  
  11.提交容器的镜像（在容器内部）
  docker commit 容器id 容器名称
  
  12.保存（压缩）镜像文件
  docker save 镜像id > 镜像压缩文件
  
  13.镜像文件导入
  docker load < 镜像压缩文件
  ```



- dockerfile

  ```
  from             # 继承容器镜像
  workdir			 # 进入容器目录
  add				 # 添加文件到容器   ！！！注意压缩包会自动解压缩
  run 			 # 执行linux命令
  copy			 # 复制文件到容器
  env 			 # 环境变量
  
  ```

  