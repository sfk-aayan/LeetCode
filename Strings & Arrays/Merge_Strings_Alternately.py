class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) >= len(word2):
            flag = True
            maxLen = len(word1)
        else:
            flag = False
            maxLen = len(word2)
        ans = ''
        if flag:
            for i in range(maxLen):
                ans += word1[i]
                if i < len(word2):
                    ans += word2[i]
        else:
            for i in range(maxLen):
                if i < len(word1):
                    ans += word1[i]
                ans += word2[i]

        return ans