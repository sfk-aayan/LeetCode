# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ct = 0
        
        def dfs(root, curMax):
            nonlocal ct
            if not root:
                return

            if root.val >= curMax:
                curMax = root.val
                ct += 1

            dfs(root.left, curMax)
            dfs(root.right, curMax)
            
        dfs(root, root.val)

        return ct