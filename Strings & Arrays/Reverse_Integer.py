class Solution:
    def reverse(self, x: int) -> int:
        s = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            temp = x % 10
            s = s * 10 + temp * sign
            x = x // 10

        return s if s <= pow(2, 31) and s >= pow(-2, 31) else 0

        