class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        map1 = set(nums1)
        map2 = set(nums2)

        res = [[], []]

        for item in map1:
            if item not in map2:
                res[0].append(item)
        
        for item in map2:
            if item not in map1:
                res[1].append(item)

        return res
