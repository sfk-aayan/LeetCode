class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        lenn = len(grid[0])
        ct = collections.defaultdict(int)
        for row in grid:
            ct[tuple(row)] += 1

        ans = 0
        for i in range(lenn):
            col = []
            for j in range(lenn):
                col.append(grid[j][i])
            if tuple(col) in ct:
                ans += ct[tuple(col)]

        return ans

            

        