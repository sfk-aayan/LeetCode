class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > 0 and len(word2) == 0:
            return len(word1)
        
        dp = []
        for i in range(len(word1)+1):
            dp.append([float('inf')] * (len(word2)+1))

        dp[0][0] = 0

        for i in range(1, len(word1)+1):
            dp[i][0] = 1 + dp[i-1][0]

        for i in range(1, len(word2)+1):
            dp[0][i] = 1 + dp[0][i-1]

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))

        return dp[-1][-1]