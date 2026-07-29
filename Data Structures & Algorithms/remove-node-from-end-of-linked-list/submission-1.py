# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursions naturally start processing the linked list from the end, and the call stack would take a o(n) space complexity

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def remove(head, n):
            if not head:
                return None

            head.next = remove(head.next, n)

            n[0] -= 1
            if n[0] == 0:
                return head.next

            return head
        
        return remove(head, [n])

        