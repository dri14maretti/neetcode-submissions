# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def backtracking(node, remaining):
            if not node:
                return False
            if node.left == None and node.right == None:
                print(node.val)
                return remaining - node.val == 0 
            
            right, left = False, False

            if node.right != None:
                right = backtracking(node.right, remaining - node.val)
            if node.left != None:
                left = backtracking(node.left, remaining - node.val)
            
            return right or left

        return backtracking(root, targetSum)