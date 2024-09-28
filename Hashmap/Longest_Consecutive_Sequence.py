class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        Set = set(nums)

        MaxLen = 0
        for item in nums:
            if item - 1 not in Set:
                result = 0
                while item in Set:
                    result += 1
                    item += 1
                MaxLen = max(MaxLen, result)
        
        return MaxLen




            

        

        