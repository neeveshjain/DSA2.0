class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode

    def isEmpty(self):
        if self.linkedlist == None:
            return True
        return False

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            tempNode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return tempNode

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.linkedlist.head

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None



custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print(custQueue.dequeue())
print(custQueue)
