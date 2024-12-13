class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def bSearch(row, left, right):
            mid = (left + right) // 2

            if left > right:
                return False

            if matrix[row][mid] == target:
                return True

            if target > matrix[row][mid]:
                return bSearch(row, mid + 1, right)
            else:
                return bSearch(row, left, mid - 1)

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            if bSearch(i, 0, col - 1):
                return True

        return False
    
        