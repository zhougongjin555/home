# 栈---
class Stack():
    def __init__(self):
        self.item = list()

    def isEmpty(self):
        return len(self.item) == 0

    def push(self, num):
        self.item.append(num)
        return self.item

    def pop(self):
         return self.item.pop()

    def size(self):
        return len(self.item)
