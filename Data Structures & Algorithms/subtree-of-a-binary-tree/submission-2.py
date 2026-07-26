# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compareBfs(root, subRoot):
            if root is None:
                return False
            queue = deque([root])
            subRootQueue = deque([subRoot])

            while queue and subRootQueue:
                node = queue.popleft()
                subNode = subRootQueue.popleft()
                if node.val != subNode.val:
                    return False
                
                if node.right: 
                    queue.append(node.right)
                if subNode.right:
                    subRootQueue.append(subNode.right)
                if node.left: 
                    queue.append(node.left)
                if subNode.left:
                    subRootQueue.append(subNode.left)
            return not(queue or subRootQueue)

        res = False
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                res = compareBfs(node, subRoot)

            if res:
                break
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
            
        