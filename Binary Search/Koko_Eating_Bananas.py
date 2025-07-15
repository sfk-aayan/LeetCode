class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(speed):
            total = 0
            for pile in piles:
                total += ceil(pile/speed)

            return total <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left+right) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left