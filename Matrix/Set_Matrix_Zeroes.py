class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowLen = len(matrix)
        colLen = len(matrix[0])
        zeroCheck = []

        for i in range(rowLen):
            for j in range(colLen):
                if matrix[i][j] == 0:
                    zeroCheck.append((i, j))
        
        for row, col in zeroCheck:
            for i in range(colLen):
                matrix[row][i] = 0

            for j in range(rowLen):
                matrix[j][col] = 0

        