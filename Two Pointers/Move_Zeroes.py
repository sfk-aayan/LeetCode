class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        i = 0
        j = i + 1

        while j < len(nums):
            if nums[i] == 0:
                if j < len(nums) and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            else:
                i += 1
            j += 1

        return nums