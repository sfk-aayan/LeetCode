class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minSum = []
        for i in range(len(triangle)):
            minSum.append([(float('inf'))]*len(triangle[i]))
        
        minSum[0][0] = triangle[0][0] 

        for i in range(1, len(triangle)): 
            for j in range(len(triangle[i])):
                if j == 0:
                    minSum[i][j] = min(minSum[i][j], minSum[i-1][j] + triangle[i][j])
                else:
                    if j < len(triangle[i-1]):
                        minSum[i][j] = min(minSum[i][j], minSum[i-1][j] + triangle[i][j])
                    minSum[i][j] = min(minSum[i][j], minSum[i-1][j-1] + triangle[i][j])
                    
        return min(minSum[-1])