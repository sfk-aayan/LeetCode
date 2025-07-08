# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minn = float('inf')
        prev = None

        def dfs(root):
            if not root:
                return 

            dfs(root.left)
            nonlocal minn, prev

            if prev:
                minn = min(minn, abs(root.val - prev.val))

            prev = root
            dfs(root.right)

        dfs(root)
        return minn
            
        