class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = {(m-1, n-1):1}
        
        def recursion(i, j):
            if i>=m or j>=n or obstacleGrid[i][j]==1:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i, j)] = recursion(i+1, j) + recursion(i, j+1)
            return dp[(i, j)]

        return recursion(0,0)

