class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lenn = len(nums)

        for i in range(lenn):
            nums.append(nums[i])

        return nums