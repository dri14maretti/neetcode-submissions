# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resHead = ListNode()
        resIt = resHead
        leftover = 0

        while l1 or l2 or leftover != 0:
            nextL1 = l1.val if l1 else 0
            nextL2 = l2.val if l2 else 0
            newNode = nextL1 + nextL2 + leftover
            
            if newNode // 10 > 0:
                newNode -= 10
                leftover = 1
            else:
                leftover = 0

            resIt.next = ListNode(newNode)

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            resIt = resIt.next

        return resHead.next