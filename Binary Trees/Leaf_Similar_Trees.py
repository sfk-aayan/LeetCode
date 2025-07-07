# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = []
        seq2 = []

        def dfs(root, flag):
            nonlocal seq1, seq2

            if not root:
                return
            if not root.left and not root.right:
                seq1.append(root.val) if flag else seq2.append(root.val)

            dfs(root.left, flag)
            dfs(root.right, flag)
            return

        dfs(root1, True)
        dfs(root2, False)

        return seq1 == seq2
