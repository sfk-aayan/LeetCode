class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return n

        if n == 2:
            return 2

        if n == 3:
            return 5
        
        arr = [0] * (n+1)
        arr[1] = 1
        arr[2] = 2
        arr[3] = 5

        for i in range(4, n+1):
            arr[i] = (2 * arr[i-1]) + arr[i-3]

        return arr[n] % (pow(10, 9) + 7)