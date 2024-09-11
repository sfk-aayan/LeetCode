class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        minLen = float("inf")
        sum = 0
        
        while right < len(nums):
            sum += nums[right]
            
            while sum >= target:
                minLen = min(minLen, right - left + 1)
                sum -= nums[left]
                left += 1

            right += 1
            
        return 0 if minLen == float("inf") else minLen