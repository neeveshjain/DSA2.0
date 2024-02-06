class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next


# Driver code
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Create linked lists
l1 = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)

l2 = ListNode(2)
l2.next = ListNode(4)
l2.next.next = ListNode(6)

print("Original lists:")
print("List 1: ", end="")
printList(l1)
print("List 2: ", end="")
printList(l2)

merged_list = mergeTwoLists(l1, l2)

print("\nMerged list:")
printList(merged_list)
