class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        currMax = max(candies)

        for item in candies:
            res.append(item + extraCandies >= currMax)

        return res