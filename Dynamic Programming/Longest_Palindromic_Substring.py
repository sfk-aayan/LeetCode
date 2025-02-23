class Solution(object):
    def longestPalindrome(self, s):
        length = len(s)

        if length <= 1:
            return s
            
        table = [[False for _ in range(length)] for _ in range(length)]
        max_len = 1
        max_str = s[0]

        for i in range(length):
            table[i][i] = True
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or table[j + 1][i - 1]):
                    table[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i - j + 1
                        max_str = s[j: i + 1]

        return max_str


# Other Method
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        mLen = 0
        res = ""

        for i in range(len(s)-1):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > mLen:
                    res = s[l:r+1]
                    mLen = len(s[l:r+1])

                l -= 1
                r += 1

            l, r = i, i+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > mLen:
                    res = s[l:r+1]
                    mLen = len(s[l:r+1])

                l -= 1
                r += 1

        return res
        










































        