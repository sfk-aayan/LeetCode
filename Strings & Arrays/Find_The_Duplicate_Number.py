class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = set()

        for no in nums:
            if no in check:
                return no
            else:
                check.add(no)