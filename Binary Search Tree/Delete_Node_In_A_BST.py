# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        def helper(root):
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right

            cur = root
            leftMost = root.left
            right = root.right

            while leftMost.right:
                leftMost = leftMost.right

            leftMost.right = right

            return cur.left

        if root.val == key:
            return helper(root)

        cur = root

        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = helper(root.left)
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = helper(root.right)
                else:
                    root = root.right

        return cur