class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bSearch(left, right):
            mid = (left + right) // 2

            if left > right:
                return -1

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                return bSearch(mid + 1, right)
            else:
                return bSearch(left, mid - 1)

        l, r = 0, len(nums) - 1
        nl, nr = 0, len(nums) - 1

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                r = i
                nl = i + 1
        
        if l == nl and r == nr:
            return bSearch(l, r)
        else:
            res1 = bSearch(l, r)
            res2 = bSearch(nl, nr)

            if res1 != -1:
                return res1
            elif res2 != -2:
                return res2
            return -1
                        