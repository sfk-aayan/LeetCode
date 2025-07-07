# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ct = 0
        pathSum = defaultdict(int)
        pathSum[0] = 1
        def dfs(root, pathSum, curSum):
            nonlocal ct, targetSum
            if not root:
                return

            curSum += root.val
            val = curSum - targetSum
            ct += pathSum[val]

            pathSum[curSum] += 1

            dfs(root.left, pathSum, curSum)
            dfs(root.right, pathSum, curSum)

            pathSum[curSum] -= 1

        dfs(root, pathSum, 0)

        return ct