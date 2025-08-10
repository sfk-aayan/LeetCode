class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 1 and len(text2) == 1:
            return 1 if text1[0] == text2[0] else 0
        
        len1 = len(text1)
        len2 = len(text2)

        arr = [[0] * (len2+1) for _ in range(len1+1)]

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1] == text2[j-1]:
                    arr[i][j] = arr[i-1][j-1] + 1
                else:
                    arr[i][j] = max(arr[i][j-1], arr[i-1][j])

        return arr[len1][len2]