class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen = len(needle)
        hayLen = len(haystack)

        if needleLen > hayLen:
            return -1

        return haystack.find(needle)