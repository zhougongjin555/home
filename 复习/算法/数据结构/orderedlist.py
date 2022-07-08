class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList():
    def __init__(self):
        self.head = None

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() < item:
                previous = current
                current = current.getNext()
            else:
                stop = True
        temp = Node(item)
        if current is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            previous.setNext(temp)
            temp.setNext(current)


    def search(self, item):
        current = self.head
        found = False
        count = 0
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                if current.getData > item:
                    return "not found!"
                else:
                    count += 1
                    current = current.getNext()
        return "item at index:" + str(count)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def isEmpty(self):
        return self.head is None

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current is None:
                return "not found"
            if current.getData() == item:
                found = True
            previous = current
            current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return item + "removed!"
