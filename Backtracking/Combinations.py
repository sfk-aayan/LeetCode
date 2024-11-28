class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backTrack(index, arr):
            if len(arr) == k:
                res.append(arr.copy())
                return

            for item in range(index, n + 1):
                arr.append(item)
                backTrack(item + 1, arr)
                arr.pop()

        backTrack(1, [])
        return res