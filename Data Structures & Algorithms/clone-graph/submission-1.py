"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeRef = {}
        visited = set()
        def copyNode(node: 'Node'):
            if not node:
                return None       
            if node.val in nodeRef:
                return nodeRef[node.val]

            newNode = Node(node.val)
            nodeRef[node.val] = newNode

            for n in node.neighbors:
                newNode.neighbors.append(copyNode(n))

            return newNode

        return copyNode(node)
        