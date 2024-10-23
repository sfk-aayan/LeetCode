# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0.000]
            
        q = deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)
            ans = 0

            for _ in range(qLen):

                node = q.popleft()
                ans += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(ans/qLen)

        return res
        