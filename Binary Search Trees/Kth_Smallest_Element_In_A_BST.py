# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root.left and not root.right:
            return root.val

        ct = 1
        ele = root.val

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            nonlocal ct, k, ele

            if ct == k:
                ele = root.val

            ct += 1

            dfs(root.right)

        dfs(root)
        return ele
        