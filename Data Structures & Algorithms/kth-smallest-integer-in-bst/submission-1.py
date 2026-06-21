# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self, count = 0, res = 0):
        self.count = count
        self.res = res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.res = root.val

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            self.count -= 1
            if self.count == 0:
                self.res = root.val
                return
            dfs(root.right)

        dfs(root)

        return self.res
        