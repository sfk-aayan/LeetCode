class Solution:
    def rob(self, nums: List[int]) -> int:
        lenn = len(nums)

        if lenn == 1:
            return nums[0]
        
        if lenn == 2:
            return max(nums[0], nums[1])

        prev = nums[0]
        nxt = max(nums[0], nums[1])

        for i in range(2, lenn):
            prev, nxt = nxt, max(nxt, prev + nums[i])

        return nxt