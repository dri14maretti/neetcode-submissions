"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        originalToCopied = {None: None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            originalToCopied[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = originalToCopied[cur]
            copy.next = originalToCopied[cur.next]
            copy.random = originalToCopied[cur.random]
            cur = cur.next
        
        
        return originalToCopied[head]