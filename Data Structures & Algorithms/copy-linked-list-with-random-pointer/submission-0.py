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
        randomPtrs = {}
        
        node = head
        saveHeadFlag = True
        newHead = None
        newNode = None
        prev = None
        while node:
            newNode = Node(node.val)

            if saveHeadFlag:
                newHead = newNode
                saveHeadFlag = False

            if node.random:
                if node.random in randomPtrs:
                    randomPtrs[node.random].append(newNode)
                else:
                    randomPtrs[node.random] = [newNode]
            
            if prev:
                prev.next = newNode

            prev = newNode
            node = node.next

        node = head
        newNode = newHead
        while node:
            if node in randomPtrs:
                for randomPtr in randomPtrs[node]:
                    randomPtr.random = newNode

            node = node.next
            newNode = newNode.next


        return newHead