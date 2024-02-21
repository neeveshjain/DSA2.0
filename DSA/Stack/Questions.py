#Use a single python list to implement 3 stacks.
class Multistack:
    def __init__(self,stacksize):
        self.numberstacks = 3
        self.custList = [0] * (stacksize*self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksizes = stacksize

    def isFull(self,stacknum):
        if self.sizes[stacknum] == self.stacksizes:
            return True
        else:
            return False

    def isEmpty(self,stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False

    def indexOfTop(self,stacknum):
        offset = stacknum * self.stacksizes
        return offset + self.sizes[stacknum] - 1

    def push(self,item,stacknum):
        if self.isFull(stacknum):
            return "The Stack is Full"
        else:
            self.sizes[stacknum] += 1
            self.custList[self.indexOfTop(stacknum)] = item

    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            return "Stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            self.custList[self.indexOfTop(stacknum)] = 0
            self.sizes[stacknum] -= 1
            return value

    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            return "Stack is empty"
        else:
            value = self.custList[self.indexOfTop(stacknum)]
            return value

custStack = Multistack(6)
print(custStack.isFull(0))
print(custStack.isEmpty(1))
custStack.push(1,0)
custStack.push(2,0)
custStack.push(3,2)
print(custStack.peek(2))
