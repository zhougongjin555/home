import multiprocessing




def task(q):
    for i in range(10):
        q.put(i)


if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=task, args=(queue,))
    p.start()
    p.join()

    print("主进程")
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())
    print(queue.get())


from threading import Thread
from multiprocessing import Process
def task(a,b):
    pass
a = Process(target=task, args=(1,2,))
a.daemon = True
a.start()
a.join()