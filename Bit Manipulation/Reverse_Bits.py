class Solution:
    def reverseBits(self, n: int) -> int:
        reverseN = 0
        for _ in range(32):
            reverseN = reverseN << 1
            bit = n & 1
            reverseN = reverseN | bit
            n = n >> 1

        return reverseN
        