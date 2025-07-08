# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def dfs(root):
            if root is None or root.val == val:
                return root

            left = None
            right = None
            if val < root.val:
                left = dfs(root.left)
            else:
                right = dfs(root.right)

            return left or right

        return dfs(root)