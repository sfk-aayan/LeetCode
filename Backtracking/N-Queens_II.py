class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0] * n] * n
        ct = 0
        visitedCols = set()
        posDia = set()
        negDia = set()

        def backTrack(col, row):
            nonlocal ct
            if row == n:
                ct += 1
                return

            for i in range(n):
                pos = row + i
                neg = row - i

                if i in visitedCols or pos in posDia or neg in negDia:
                    continue

                visitedCols.add(i)
                posDia.add(pos)
                negDia.add(neg)

                backTrack(i, row + 1)

                visitedCols.remove(i)
                posDia.remove(pos)
                negDia.remove(neg)

        backTrack(0, 0)
        return ct