# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listHead = ListNode(0, ListNode(0, None))
        nextNewList = listHead.next
        while(list1 or list2):
            if list2 is not None and (list1 is None or list1.val > list2.val):
                nextEl = list2.val
                list2 = list2.next
            else:
                nextEl = list1.val
                list1 = list1.next
            
            nextNewList.next = ListNode()
            nextNewList = nextNewList.next
            nextNewList.val = nextEl

        return listHead.next.next

        