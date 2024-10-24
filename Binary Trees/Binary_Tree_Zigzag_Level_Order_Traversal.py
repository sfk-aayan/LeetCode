# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)

        res = []
        isLeft = True

        while q:

            qLen = len(q)
            store = []

            for _ in range(qLen):
                node = q.popleft()
                store.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if isLeft == True:
                isLeft = False
            else:
                store.reverse()
                isLeft = True

            res.append(store)

        return res


        