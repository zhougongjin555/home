class MyQueue():
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def enqueue(self, it):
        self.item.insert(0, it)
        return self.item

    def dequeue(self):
        return self.item.pop()

