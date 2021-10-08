# coding ：UTF-8
# 开发人员： Administrator
# 开发时间： 2021/9/14 14:47
# 文件名称： 数据结构.py
# 文件地址： 
# 开发工具： PyCharm
# 开发功能：

from collections import deque

class Stack:
    '''栈'''
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


def brace_match(s):
    '''判断括号是否匹配'''
    match = {'}':'{', ']':"[", ')':'('}
    stack = Stack()
    for ch in s:
        if ch in {'(','[','{'}:
            stack.push(ch)
        else:   #ch in {'}',']',')'}
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:
                stack.pop()
            else: # stack.get_top() != match[ch]
                return False
    if stack.is_empty():
        return True
    else:
        return False



#############################################################

class Queue:
    '''队列'''
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0 # 队首指针

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled.")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")

    # 判断队空
    def is_empty(self):
        return self.rear == self.front

    # 判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


# 双向队列内置模块

# q = deque([1,2,3,4,5], 5) # 超出队列后，自动踢去第一个，然后进入
# q.append(12)
# print(q)
# q.appendleft(13)
# print(q)
# print(q.popleft())


# 栈和队列解决迷宫问题
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
dirs = [
    lambda x, y: (x+1, y),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y-1),
    lambda x, y: (x, y+1),
]


def maze_path(x1,y1,x2,y2):
    '''
    栈： 深度优先搜索
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    '''
    stack = []
    stack.append((x1, y1))
    while(len(stack) > 0):
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stack:
                print(p)
            return True
        # 找四个方向：
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下位置可行
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2  # 表示已经经过
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print('no ways')
        return False

# maze_path(1,1,8,8)

def print_r(path):
    real_path = []
    i = len(path) - 1
    while i >= 0:
        real_path.append(path[i][0:2])
        i = path[i][2]
    real_path.reverse()
    for node in real_path:
        print(node)


def maze_path_queue(x1,y1,x2,y2):
    '''
    队列： 广度优先搜索
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    '''
    queue = deque()
    path = []
    queue.append((x1, y1, -1))
    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)

        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True

        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下位置可行
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))
                maze[nextNode[0]][nextNode[1]] = 2  # 表示已经经过
    return False

# maze_path_queue(1,1,8,8)


###########################################
# 链表
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next

# lk = create_linklist_tail([1,2,3,6,8])
# print_linklist(lk)












