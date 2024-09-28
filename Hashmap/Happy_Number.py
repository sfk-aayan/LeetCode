class Solution:
    def isHappy(self, n: int) -> bool:
        hMap = {}
        hMap[n] = 1

        while hMap[n] == 1:
            result = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                result += digit
                n = n // 10

            n = result
            hMap[n] = hMap.get(n, 0) + 1
            if n == 1:
                return True

        return False 

 

        
        