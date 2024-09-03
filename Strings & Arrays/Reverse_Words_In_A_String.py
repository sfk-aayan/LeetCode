class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(reversed(s.split()))
        return s

        
        