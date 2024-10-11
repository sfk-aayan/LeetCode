# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if (p and not q) or (q and not p):
            return False

        if p.val != q.val:
            return False

        check1 = self.isSameTree(p.left, q.left) 
        check2 = self.isSameTree(p.right, q.right) 
        
        return True if check1 == True and check2 == True else False 
        