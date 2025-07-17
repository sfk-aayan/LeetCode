class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(index, curSum, curVals):
            if curSum == n and len(curVals) == k:
                res.append(curVals[:])
                return

            for i in range(index, 10):
                curVals.append(i)
                dfs(i+1, curSum+i, curVals)
                curVals.pop()
            return

        dfs(1, 0, [])

        return res