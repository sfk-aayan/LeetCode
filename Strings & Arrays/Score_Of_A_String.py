class Solution:
    def scoreOfString(self, s: str) -> int:
        sm = 0
        for i in range(len(s)):
            if i + 1 < len(s):
                sm += abs(ord(s[i]) - ord(s[i+1]))

        return sm
        