class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        boardLen = len(board)
        board.reverse()

        def getCor(s):
            r = (s - 1) // boardLen
            c = (s - 1) % boardLen

            if r % 2:
                c = boardLen - 1 - c

            return r, c

        q = deque()
        visit = set()
        q.append((1, 0)) 
    
        while q:
            square, moves = q.popleft()

            for i in range(1, 7):
                cur_square = square + i
                r, c = getCor(cur_square)

                if board[r][c] != -1:
                    cur_square = board[r][c]

                if cur_square == boardLen * boardLen:
                    return moves + 1

                if cur_square not in visit:
                    visit.add(cur_square)
                    q.append((cur_square, moves + 1))

        return -1