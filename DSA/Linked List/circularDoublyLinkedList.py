class Node:
    def __init__(self,value):
        self.value = value
        self.head = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head= newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "Done"

circularDL = CircularDoublyLinkedList()
circularDL.createDLL(5)
print([node.value for node in circularDL])