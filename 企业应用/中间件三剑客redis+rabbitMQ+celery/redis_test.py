# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/28 10:42
# 文件名称： redis_test.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能：

''':cvar
博客地址：https://www.cnblogs.com/pyedu/p/12452407.html
'''








import time
import redis

# 基本连接方式
# rb = redis.Redis(host='127.0.0.1', port=6379)

# 连接池连接方式   (避免一直无用的重复连接对象)
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
rp = redis.Redis(connection_pool=pool)

# -------------------------------------------字符串常用操作

rp.set("name", 'zhougongjin', ex=5)  # ex设置过期时间 （秒）
for i in range(6):
    print(rp.get('name'))
    time.sleep(1)

# 批量设置
rp.mset({'k1': 'v1', 'k2': 'v2'})
rp.mget(['k1', 'k2'])

# 取原值并设置新值
rp.getset('name', 'zhugeliang')

# 设置，获取字符串指定位置
rp.getrange('name', 3, 5)
rp.setrange('name', 3, "###")

# 获取字符串的长度
rp.strlen('name')

# 自增/自减操作
rp.set('age', 10)
rp.incr('age', amount=3)
rp.incrbyfloat('age', amount=3.1)   # 浮点型

rp.decr('age', amount=4)

# 字符串追加
rp.append('name', ' wo_ai_ni')



# -------------------------------------------哈希常用操作

# 设置键值对
rp.hset('info', 'name', 'zhougongjin')

rp.hget('info', 'name')
rp.hgetall('info')



# 批量设置
rp.hmset('infos', {'name': 'zhouzhou', 'age': 100, "sex": 'male'})
rp.hmget('infos', ['name', 'sex'])
rp.hgetall('infos')



# 获取键值对个数
rp.hlen('infos')


# 判断是否存在某个键值对
rp.hexists('infos', 'name')


# 获取key   value值
rp.hkeys('infos')
rp.hvals('infos')


# 删除指定键值对
rp.hdel('infos', 'sex')
rp.hgetall('infos')


# 自增
rp.hincrby('infos', 'age', amount=2)
rp.hincrbyfloat('infos', 'age', amount=-2.5)


# 生成器、迭代获取数据
all_data = rp.hscan_iter('infos')
for i in all_data:
    print(i)

# -------------------------------------------链表(列表)常用操作
# 设置和取值
rp.lpush('a1', 55, 66, 77, 22)
rp.lrange('a1', 0, -1)

rp.rpush('a2', 11, 22, 33, 44)
rp.lrange('a2', 0, -1)

# name存在时,添加到最左//最右边
rp.lpushx('a1', 22)
rp.rpushx('a1', 0)

# 获取列表元素的个数
rp.llen('a1')

# 向某一个值前后插入一个值
rp.linsert('a1', 'after', '77', '88')
rp.linsert('a1', 'before', '22', 'xxxx')
rp.linsert('a1', 'after', '22', 'xxxx')
rp.lrange('a1', 0, -1)


# 重新赋值
rp.lset('a1', 0, 100)

# 删除元素
rp.lrem(name='a1', count=0, value='22')    # count=0, 删除所有的值， count=n，从前往后删除n个

# 从左，右弹出一个元素
rp.lpop('a1')
rp.rpop('a1')

# 根据索引获取对应元素
rp.lindex('a1', 0)

# 移除所取范围之外的所有元素
rp.ltrim('a1', 2, 4)


# -------------------------------------------集合(无序)常用操作
# 添加查看元素
rp.sadd('set1', 1, 2, 8, 4, 6, 7, 3, 6, 5, 1)   # 会自动去重
rp.smembers('set1')

# 获取集合元素个数
rp.scard('set1')

# 在第一个集合，并且不在第二个集合中的元素(差集)
rp.sadd('set2', 1, 3, 6, 5, 1, 11, 23, 55)
rp.sdiff('set1', 'set2')

# 获取两个集合的交集，并集
rp.sinter('set1', 'set2')
rp.sunion('set1', 'set2')

# 检查是否是集合的成员
rp.sismember('set1', 100)

# 随机弹出来一个元素
rp.spop('set1')

# 随机获取n个元素
rp.srandmember(name='set1', number=3)

# 从集合中删除元素
rp.srem('set1', 55)

# 迭代器，分批获取数据
data = rp.sscan_iter('set1')
for _ in data:
    print(_)
    
    
# -------------------------------------------集合(有序)常用操作
# 添加查看元素
rp.zadd('zset1', {'n1': 1, 'n2': 55, 'n3': 8, 'n4': 46, 'n5': 22, 'n6': 45, 'n7': 66})
rp.zscan('zset1')

# 查看元素个数
rp.zcard('zset1')

# 查看分数在min, max之间的元素的个数
rp.zcount(name='zset1', min=10, max=100)

# 分数自增
rp.zincrby(name='zset1', amount=100, value='n2')

# 获取某个索引范围内的数据
rp.zrange('zset1', 1, 5)

# 获取某个元素的分数
rp.zscore('zset1', 'n3')

# 获取某个元素的排行////索引
rp.zrank(name='zset1', value='n6')

# 删除元素
rp.zrem('zset1', 'n1')

# 根据排名、分数范围删除，删除范围内部的元素
rp.zremrangebyrank('zset1', 0, 1)
rp.zremrangebyscore('zset1', 10, 1000)

# 交集、并集
rp.zadd('zset2', {'n1': 10, 'n2': 22, 'n11': 22, "x1": 0})
rp.zinterstore('zset3', ('zset1', 'zset2'), 'sum')   # (新集合， （比较的集合）， 相同元素的处理方式（'sum' \ 'min' \ 'max'）)
rp.zunionstore('zset4', ('zset1', 'zset2'), 'sum')
rp.zscan('zset3')
rp.zscan('zset4')

# ---------------------------------------------其他常用操作
# 看看所有的键（name）
rp.keys()
rp.keys(pattern='z*')

# 删除某个键（name）
rp.delete('zset3')

# 查看是否存在某个键
rp.exists('zset1')

# 为某个键设置过期时间(秒)
rp.expire('zset1', 60)

# 为键重命名
rp.rename('k1', 'k1')

# 获取键的类型
rp.type('set1')


# 管道操作（事务），同时成功，同时失败
pipe = rp.pipeline(transaction=True)

pipe.set('name', 'alex')
pipe.set('role', 'sb')

pipe.execute()

# 发布订阅功能
# 发布
rp.publish('name', 'zhougongjin')

# 订阅
pub = rp.pubsub()
pub.subscribe('name')

while 1:
    msg = pub.parse_response()
    print(msg)
