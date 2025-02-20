class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        prev, nxt = 1, 2

        for i in range(2, n):
            prev, nxt = nxt, prev + nxt

        return nxt