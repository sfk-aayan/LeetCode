class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum = 0
        
        for item in nums:
            curSum += item
            if curSum > maxSum:
                maxSum = curSum
            if curSum < 0:
                curSum = 0

        return maxSum