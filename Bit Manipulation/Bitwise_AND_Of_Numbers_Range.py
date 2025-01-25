class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ctr = 0

        while left != right:
            left >>= 1
            right >>= 1
            ctr += 1

        return left << ctr