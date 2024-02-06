# ↓↑    -> LIFO
# _
# _
# _
# _
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def append(self,value):
        self.list.append(value)
        return "Done Successfully"
    def pop(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None


customStack = Stack()
customStack.append(4)
customStack.append(5)
customStack.append(6)
print(customStack.peek())
print('-------------------------')
print(customStack)