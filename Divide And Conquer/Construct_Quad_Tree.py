"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        
        def recursion(n, r, c):
            isSame = True

            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r+i][c+j]:
                        isSame = False
                        break
            
            if isSame:
                return Node(grid[r][c], True, None, None, None, None)

            n = n // 2

            topLeft = recursion(n, r, c)
            topRight = recursion(n, r, c + n)
            bottomLeft = recursion(n, r + n, c)
            bottomRight = recursion(n, r + n, c + n)

            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        return recursion(n, 0 , 0)