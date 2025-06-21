class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i_max = float('inf')
        j_max = float('inf')

        for item in nums:
            if item <= i_max:
                i_max = item
            elif item <= j_max:
                j_max = item
            else:
                return True
        return False 