class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bSearch(left, right):
            mid = (left + right) // 2

            if left > right:
                return [-1, -1]

            if nums[mid] == target:
                ctr = minMid = maxMid = mid
                while ctr > 0 and nums[ctr - 1] == target:
                    ctr -= 1
                    minMid = ctr
                ctr = mid
                while ctr < len(nums) - 1 and nums[ctr + 1] == target:
                    ctr += 1
                    maxMid = ctr
                
                return [minMid, maxMid]

            if target > nums[mid]:
                return bSearch(mid + 1, right)
            else:
                return bSearch(left, mid - 1)

        return bSearch(0, len(nums) - 1)
        