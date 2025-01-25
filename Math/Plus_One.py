class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits) - 1
        carry = 0
        while l >= 0:
            if digits[l] < 9:
                digits[l] += 1
                return digits
            digits[l] = 0

            l -= 1

        digits.insert(0, 1)
        return digits

        
            

            

            