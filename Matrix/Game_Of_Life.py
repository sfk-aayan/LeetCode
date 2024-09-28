class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowLen = len(board)
        colLen = len(board[0])

        directions = [[-1, -1], [-1, 0], [0, -1], [1, 0], [0, 1], [1, 1], [1, -1], [-1, 1]]

        for i in range(rowLen):
            for j in range(colLen):

                count = 0

                for dir in directions:
                    rowPt = i + dir[0]
                    colPt = j + dir[1]
                    
                    if (rowPt >= 0 and rowPt < rowLen and colPt >= 0 and colPt < colLen and 
                    (board[rowPt][colPt] == 1 or board[rowPt][colPt] == 2)):
                        count += 1

                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 2
                else:
                    if count == 3:
                        board[i][j] = 3

        for i in range(rowLen):
            for j in range(colLen):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1


        
        