# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def invertLinkedList(listhead):
            last = None 
            it = listhead

            while it:
                stored = it.next
                it.next = last
                last = it
                it = stored

            return last

        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        last = invertLinkedList(slow)
        it = head

        while it:
            stored = it.next
            it.next = last
            storedLast = last.next
            last.next = stored
            it = stored
            last = storedLast
        
        