class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backTrack(index, arr):

            if sum(arr) == target:
                res.append(arr.copy())
                return

            if index >= len(candidates) or sum(arr) > target:
                return

            arr.append(candidates[index])
            backTrack(index, arr)
            arr.pop()        
            backTrack(index + 1, arr)

        backTrack(0, [])
        return res
        