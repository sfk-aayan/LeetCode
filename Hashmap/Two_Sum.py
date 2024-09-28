class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        result = []

        for i, n in enumerate(nums):
            if target - n in hMap:
                return [hMap[target - n], i]
            hMap[n] = i

        
            
        