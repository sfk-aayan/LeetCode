# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ct = []
        ct.append(0)

        def dfs(root, ct):
            if not root:
                return

            dfs(root.left, ct)

            ct[0] += 1

            dfs(root.right, ct)

        dfs(root, ct)
        return ct[0]
        