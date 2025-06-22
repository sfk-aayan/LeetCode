class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLen = float('-inf')
        zeroes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)

        return maxLen
