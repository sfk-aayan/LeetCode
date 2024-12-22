import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for i in range(len(nums)):
            item = -heappop(nums)

            if i == k - 1:
                return item