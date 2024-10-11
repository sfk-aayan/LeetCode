# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursion(self, left, right):
        if not left and not right:
            return True

        if (left and not right) or (not left and right):
            return False

        if left.val != right.val:
            return False

        return self.recursion(left.left, right.right) and self.recursion(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans = self.recursion(root.left, root.right)
        return ans