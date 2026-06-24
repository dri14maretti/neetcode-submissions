# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head is None or head.next is None):
            return head

        countPtr = head
        size = 1
        while countPtr.next is not None:
            size += 1
            countPtr = countPtr.next

        iterations = k % size
        print(iterations)
        
        for _ in range(iterations):
            before = head
            tail = head.next
            while tail.next is not None:
                before = tail
                tail = tail.next

            before.next = None
            tail.next = head
            head = tail

        return head

        