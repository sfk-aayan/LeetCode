class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        def bSearch(left, right):
            mid = (left + right) // 2

            if left > right:
                return left

            if mid - 1 >= 0 and mid + 1 < len(nums) and nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return bSearch(left, mid - 1)
            elif mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
                return bSearch(mid + 1, right)

            return mid

        return bSearch(left, right)