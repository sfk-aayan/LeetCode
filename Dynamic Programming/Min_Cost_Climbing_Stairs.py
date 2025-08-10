class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        lenn = len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        if len(cost) <= 2:
            return min(dp[0], dp[1])

        cost.append(0)

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])

        return dp[lenn]