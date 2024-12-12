class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        flag = False
        col = len(board[0])
        row = len(board)
        visited = set()

        def backTrack(coordinates, wIndex):
            nonlocal flag

            x, y = coordinates

            if wIndex == len(word):
                flag = True
                return

            if x >= row or y >= col or x < 0 or y < 0 or wIndex >= len(word):
                return

            if board[x][y] != word[wIndex] or (x, y) in visited:
                return

            visited.add((x, y))
            for i, j in directions:
                r = x + i
                c = y + j            
                backTrack((r, c), wIndex + 1)
            
            visited.remove((x, y))

        for i in range(row):
            for j in range(col):
                if flag:
                    break
                backTrack((i, j), 0)

        return True if flag else False