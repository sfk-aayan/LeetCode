# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, maxSum):

            if not root:
                return 0

            leftSum = dfs(root.left, maxSum)
            rightSum = dfs(root.right, maxSum)
            leftSum = max(leftSum, 0)
            rightSum = max(rightSum, 0)

            maxSum[0] = max(maxSum[0], root.val + leftSum + rightSum)

            return root.val + max(leftSum, rightSum)

        maxSum = []
        maxSum.append(-10000)
        dfs(root, maxSum)
        return maxSum[0]