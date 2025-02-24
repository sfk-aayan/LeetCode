class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        states = [float('-inf')] * (2 * k)
        states[0] = -prices[0]

        for price in prices:
            for i in range(0, len(states)):
                if i == 0:
                    states[i] = max(states[i], -price)
                    continue
                
                if i % 2 != 0:
                    states[i] = max(states[i], states[i-1] + price)
                else:
                    states[i] = max(states[i], states[i-1] - price)
        
        return states[-1]