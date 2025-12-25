
class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


def find_middle(head: ListNode):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Gọi hàm và in giá trị của middle node
middle = find_middle(head)
print(middle.val)  # Output sẽ là 3