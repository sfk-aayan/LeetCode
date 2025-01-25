class Solution:
    def hammingWeight(self, n: int) -> int:
        ct = 0

        while n > 0:
            if n & 1:
                ct += 1
                
            n >>= 1

        return ct
        