class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list ==  []:
            return True
        return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False

    def push(self,value):
        if self.isFull():
            return "Stack is Full"
        else:
            self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None    

customStack = Stack(5)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(5)
print(customStack)