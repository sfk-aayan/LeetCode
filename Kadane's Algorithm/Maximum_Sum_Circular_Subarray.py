class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxSum = nums[0]
        curMaxSum = 0

        minSum = nums[0]
        curMinSum = 0
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            curMaxSum = max(nums[i], curMaxSum + nums[i])
            maxSum = max(curMaxSum, maxSum)
            curMinSum = min(nums[i], curMinSum + nums[i])
            minSum = min(curMinSum, minSum)

        maxSum = max(maxSum, total - minSum) if maxSum > 0 else maxSum
        return maxSum
        