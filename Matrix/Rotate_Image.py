class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrixLen = len(matrix)

        for i in range(matrixLen):
            for j in range(i + 1, matrixLen):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(matrixLen):
            rightPt = matrixLen - 1

            for j in range(matrixLen // 2):
                matrix[i][j], matrix[i][rightPt] = matrix[i][rightPt], matrix[i][j]
                rightPt -= 1


             

        
                

        