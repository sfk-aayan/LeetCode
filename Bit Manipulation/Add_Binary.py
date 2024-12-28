class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        carry = 0
        res = ''

        for i in range(max(len(a), len(b))):
            n1 = ord(a[i]) - ord('0') if i < len(a) else 0
            n2 = ord(b[i]) - ord('0') if i < len(b) else 0
            summ = n1 + n2 + carry
            res = res + (str(summ % 2))
            carry = (summ // 2)

        if carry != 0:
            res = res + (str(carry))

        return res[::-1]