class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
 
        arr = []
        for i in range(m):
            arr.append([float('inf')] * n)

        arr[0][0] = grid[0][0]
        for i in range(1, m):
            arr[i][0] = min(arr[i][0], arr[i-1][0] + grid[i][0])

        for i in range(1, n):
            arr[0][i] = min(arr[0][i] ,arr[0][i-1] + grid[0][i])

        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = min(arr[i][j], min(arr[i-1][j] + grid[i][j], arr[i][j-1] + grid[i][j]))

        return arr[-1][-1]
        