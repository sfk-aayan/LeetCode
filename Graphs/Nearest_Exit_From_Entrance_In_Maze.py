class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rowLen = len(maze)
        colLen = len(maze[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def bfs(src, ct):
            row, col = src
            q = deque()
            q.append(((row, col), ct))

            while q:
                node, ct = q.popleft()
                r, c = node

                if (r == rowLen - 1 or c == colLen - 1 or r == 0 or c == 0) and (r, c) != tuple(entrance):
                    return ct

                for i, j in dirs:
                    nr, nc = r + i, c + j

                    if 0 <= nr < rowLen and 0 <= nc < colLen and maze[nr][nc] == '.':
                        maze[nr][nc] = '+'
                        q.append(((nr, nc), ct+1))

            return -1

        r, c = entrance
        maze[r][c] = '+'
        return bfs(tuple(entrance), 0)