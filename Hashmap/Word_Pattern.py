class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        
        if len(s) != len(pattern):
            return False

        map1, map2 = {}, {}

        for i in range(len(s)):

            if (map1.get(s[i]) and map1[s[i]] != pattern[i]) or (map2.get(pattern[i]) and map2[pattern[i]] != s[i]):
                return False

            map1[s[i]] = pattern[i]
            map2[pattern[i]] = s[i]

        return True

        