class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set()

        for no in nums:
            if no in check:
                return True
            else:
                check.add(no)

        return False