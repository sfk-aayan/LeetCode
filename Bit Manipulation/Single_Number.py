class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for no in nums:
            res ^= no

        return res