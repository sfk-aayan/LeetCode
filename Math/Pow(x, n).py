class Solution:
    def myPow(self, x: float, n: int) -> float:
        def bSearch(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = bSearch(x, n // 2)
            res = res * res
            return x * res if n % 2 else res

        ans = bSearch(x, abs(n))

        if n >= 0:
            return ans
        else:
            return 1/ans
            
        