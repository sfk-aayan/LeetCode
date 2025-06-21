class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isDivisor(l):
            div1 = len(str1) // l
            div2 = len(str2) // l

            return str1[:l] * div1 == str1 and str2[:l] * div2 == str2 and str1[:l] == str2[:l]

        minLen = min(len(str1), len(str2))
        ans = ''
        
        for i in range(minLen, 0, -1):
            if isDivisor(i):
                return str1[:i]
            
        return ans
        