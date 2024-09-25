class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = collections.defaultdict(set)
        colMap = collections.defaultdict(set)
        subMap = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == "." or board[i][j] == ",":
                    continue 
                if board[i][j] in rowMap[i] or board[i][j] in colMap[j] or board[i][j] in subMap[(i//3, j//3)]:
                    return False
                rowMap[i].add(board[i][j])
                colMap[j].add(board[i][j])
                subMap[(i//3, j//3)].add(board[i][j])

        return True 
        