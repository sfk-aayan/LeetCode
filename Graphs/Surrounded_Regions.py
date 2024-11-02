class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        if rows == 1 and cols == 1:
            return

        visited = set()

        def dfs(i, j):
            stack = []
            stack.append((i, j))
            visited.add((i, j))
            directions = [[1,0], [0,1], [-1,0], [0,-1]]

            while stack:
                row, col = stack.pop()
                board[row][col] = "T"

                for x, y in directions:
                    r, c = x + row, y + col

                    if r in range(1, rows-1) and c in range(1, cols-1) and (r, c) not in visited and board[r][c] == "O":
                        stack.append((r, c))
                        visited.add((r,c))

        
        for i in range(rows):
            for j in range(cols):
                if (i in (0, rows - 1) or j in (0, cols - 1)) and (i, j) not in visited and board[i][j] == "O":
                    dfs(i, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"

        

        


        