class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        res = []

        def backTrack(val, arr):
            if len(arr) == len(nums):
                temp = []
                for key in arr:
                    temp.append(key)
                res.append(temp.copy())
                return

            for item in nums:
                if item not in arr:
                    arr[item] = True
                    backTrack(item, arr)
                    del arr[item]

        backTrack(nums[0], {})
        return res


        