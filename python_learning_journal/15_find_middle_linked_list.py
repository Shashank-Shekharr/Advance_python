# Find the Middle of a Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
middle = find_middle(head)
print(middle.val)  # Output: 3