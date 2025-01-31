class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif x >= mid * mid:
                left = mid + 1
            else:
                right = mid - 1

        return right 