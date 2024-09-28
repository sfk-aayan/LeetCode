class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hMap = {}
        for index, item in enumerate(nums):

            if hMap.get(item) != None and index != hMap[item] and abs(index - hMap[item]) <= k:
                return True
            
            hMap[item] =  index

        return False 
