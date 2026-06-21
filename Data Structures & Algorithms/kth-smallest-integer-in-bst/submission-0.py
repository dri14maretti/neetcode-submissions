# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            queue.append(root.val)
            print(root.val)
            dfs(root.right)

        dfs(root)

        counter = 1
        while(counter < k):
            counter += 1
            queue.popleft()

        return queue.popleft()
        