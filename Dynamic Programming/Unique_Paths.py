class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 and m == 1:
            return 1
        arr = [[0] * n for _ in range(m)]

        for i in range(m):
            arr[i][0] = 1

        for j in range(n):
            arr[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i-1][j] + arr[i][j-1]

        return arr[m-1][n-1]