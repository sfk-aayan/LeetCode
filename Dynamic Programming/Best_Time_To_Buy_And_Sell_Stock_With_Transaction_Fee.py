class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        maxProfit = 0
        res = 0
        minBuy = prices[0]

        for i in range(1, len(prices)):
            if (prices[i] - minBuy - fee) > maxProfit:
                res += (prices[i] - minBuy - fee)
                maxProfit = 0
                minBuy = prices[i]-fee
            else:
                minBuy = min(minBuy, prices[i])

        return res