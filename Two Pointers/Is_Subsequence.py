class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        if len(s) > len(t) or (t == "" and s != ""):
            return False

        if s == "":
            return True 

        while i < len(t) and j < len(s):
            if(t[i] == s[j]):
                j += 1
            i += 1

        if j == len(s):
            return True
        else:
            return False 
        