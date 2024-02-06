class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ''
        temp_node = self.head
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle(self):
        curr_node = self.head
        # TODO
        if self.length % 2 == 0:
            num = (self.length // 2)
            for _ in range(num):
                curr_node = curr_node.next
        else:
            num = (self.length // 2)
            for _ in range(num):
                curr_node = curr_node.next
        return  curr_node.value

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)
new_linked_list.append(60)
new_linked_list.append(70)
new_linked_list.append(80)
print(new_linked_list)
print(new_linked_list.find_middle())


# def find_middle(self):
#     if self.length == 0:
#         return None
#
#     slow_ptr = self.head
#     fast_ptr = self.head
#
#     while fast_ptr and fast_ptr.next:
#         slow_ptr = slow_ptr.next
#         fast_ptr = fast_ptr.next.next
#
#     return slow_ptr
