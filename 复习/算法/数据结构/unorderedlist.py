class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self):
        return "节点类"

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


#  (尾部)  head --> node(n) --> node(n-1) ...  --> node1
class UnorderedList():
    def __init__(self):
        self.head = None

    def __str__(self):
        return "链表实现无序表"

    def add(self, item):
        # 添加元素到表尾, 替换表尾，并把表尾指向新表尾
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current is None:
                return "not found"
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return item + " removed!"

    def search(self, item):
        current = self.head
        found = False
        while not found:
            if current is None:
                return "not found"
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def getList(self):
        current = self.head
        li = []
        while current is not None:
            li.append(current.getData())
            current = current.getNext()
        return li


ul = UnorderedList()
ul.add(1)
ul.add("hello")
ul.add(True)
ul.remove("hello")
ul.getList()