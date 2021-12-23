import multiprocessing
from collections import deque  # 双向队列
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Queue, Pool, Manager  # 多进程自带队列
# from queue import LifoQueue, PriorityQueue, Queue  # 普通队列，栈，优先级队列



# 多进程保持数据同步
'''
def handler(num, li):
    for i in range(num):
        li.put(i)   

if __name__ == '__main__':
    que = Queue()   # 不设置长度，默认为无限长
    p = multiprocessing.Process(target=handler, args=(50, que))
    p.daemon = False   # 是否守护子进程，如果守护，主进程已结束，守护进程跟着结束
    p.start()
    p.join()          # 测试守护进程需要不阻塞
    while not que.empty():
        print(que.get())
    print('done')
'''



def getnum(li, i):
    print(f'我是{i}进程')  # 不会打印
    print(li.get())


def done_func(res):
    print(f'200 ok {res}')   # 会打印到主进程输出界面上


if __name__ == '__main__':


    # 多个进程实现进程池
    # que = Queue()
    # for i in range(20):
    #     que.put(i)
    # print(que)
    # for i in range(10):
    #     t = multiprocessing.Process(target=getnum, args=(que, i))
    #     t.start()
    # t.join()



    # 多进程自带pool实现进程池,!!!!!!队列一定一定要使用manager里面的queue,不饿能使用多进程原生队列
    que = Manager().Queue()  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in range(20):
        que.put(i)
    print(que)
    pl = Pool(processes=10)
    # with Pool(processes = 10) as pl:
    for i in range(10):
        # res = pl.apply(getnum, (que, 0))  # 不阻塞执行
        res = pl.apply_async(getnum, (que, 0))  # 不阻塞执行
        # print(res.get())  # 返回进程池结果
    pl.close()  # 阻塞后续任务加入进程池
    pl.join()



    # xxxxxxx 目前此种进程池没好的办法实现数据交互 xxxxxx 不可用，不能返回预期结果
    # que = Manager().Queue()
    # for i in range(20):
    #     que.put(i)
    # with ProcessPoolExecutor(10) as p:
    #     for i in range(10):
    #         a = p.submit(getnum, (que, i))
    #         a.add_done_callback(done_func)
    #     p.shutdown()



    while not que.empty():
        print(que.get())
    print('done')

