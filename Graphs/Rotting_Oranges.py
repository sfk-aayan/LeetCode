class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCt = 0
        q = deque()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshCt += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if freshCt == 0:
            return 0

        steps = 0
        while q:
            size = len(q)
            rotten = False

            for _ in range(size):
                i, j = q.popleft()

                for x, y in dirs:
                    nr, nc = i + x, y + j

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        freshCt -= 1
                        rotten = True

            if rotten:
                steps += 1

        return steps if freshCt == 0 else -1