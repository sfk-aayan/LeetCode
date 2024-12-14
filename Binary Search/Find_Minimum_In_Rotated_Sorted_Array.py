class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        nl, nr = 0, len(nums) - 1

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                r = i
                nl = i + 1
                break
        
        if l == nl and r == nr:
            return nums[l]
        else:
            return min(nums[l], nums[nl])
                        
        