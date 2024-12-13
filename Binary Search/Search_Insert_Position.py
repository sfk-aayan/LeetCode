class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        def bSearch(left, right):
            mid = (left + right) // 2

            if left > right:
                return left

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                return bSearch(mid + 1, right)
            else:
                return bSearch(left, mid - 1)

        return bSearch(left, right)

        