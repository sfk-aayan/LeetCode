class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        curSum1 = 0

        minSum = float('inf')
        curSum2 = 0
        total = 0

        for item in nums:
            total += item
            curSum1 += item
            curSum2 += item

            if curSum1 > maxSum:
                maxSum = curSum1

            if curSum2 < minSum:
                minSum = curSum2

            if curSum1 < 0:
                curSum1 = 0

            if curSum2 > 0:
                curSum2 = 0

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
        