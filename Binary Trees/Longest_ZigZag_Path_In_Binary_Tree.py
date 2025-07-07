# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLen = 0
        def dfs(root, leftStart, ctr):
            nonlocal maxLen
            if root is None:
                return
            
            maxLen = max(maxLen, ctr)
            if leftStart:
                dfs(root.left, True, 1)
                dfs(root.right, False, ctr+1)
            else:
                dfs(root.right, False, 1)
                dfs(root.left, True, ctr+1)

            return
        
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)

        return maxLen