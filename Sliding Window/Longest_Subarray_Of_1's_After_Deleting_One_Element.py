class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        maxLen = 0
        ct = 0

        for right in range(len(nums)):
            if nums[right] != 1:
                ct += 1
            
            while left < len(nums) and ct > 1:
                if nums[left] != 1:
                    ct -= 1
                left += 1 
            maxLen = max(maxLen, right - left)

        return maxLen