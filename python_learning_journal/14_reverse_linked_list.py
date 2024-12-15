# Reverse a Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3)))
reversed_head = reverse_linked_list(head)
print(reversed_head.val)  # Output: 3