class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}

        if len(hashMap1) != len(hashMap2):
            return False

        for i in range(len(s)):

            if (hashMap1.get(s[i]) and hashMap1[s[i]] != t[i]) or (hashMap2.get(t[i]) and hashMap2[t[i]] != s[i]):
                return False
                
            hashMap1[s[i]] = t[i]
            hashMap2[t[i]] = s[i]

        return True

        