class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        group = s[:k]
        vowels = ('a', 'e', 'i', 'o', 'u')
        ct = 0
        for item in group:
            if item in vowels:
                ct += 1

        maxLen = ct

        for i in range(1, len(s) - k + 1):
            if s[i-1] in vowels:
                ct -= 1
            if s[i + k - 1] in vowels:
                ct += 1
            
            maxLen = max(maxLen, ct)

        return maxLen