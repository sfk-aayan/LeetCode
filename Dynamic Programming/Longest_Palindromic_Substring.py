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
        