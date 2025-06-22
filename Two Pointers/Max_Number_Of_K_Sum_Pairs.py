class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hMap = collections.defaultdict(int)
        ct = 0
        for item in nums:
            if k - item in hMap and hMap[k - item] > 0:
                hMap[k - item] -= 1
                ct += 1
            else:
                hMap[item] += 1
        
        return ct
        