# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 0
        maxVal = root.val
        maxLevel = 1

        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            s = 0
            for _ in range(qLen):
                node = q.popleft()

                s += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

            if s > maxVal:
                maxVal = s
                maxLevel = level

        return maxLevel