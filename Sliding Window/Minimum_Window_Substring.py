class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s) or t == "":
            return ""

        if s == t:
            return s

        hashMap, window = {}, {}

        for char in t:
            hashMap[char] = hashMap.get(char, 0) + 1

        minWindow = float('inf')
        minLeft = minRight = 0
        have, need = 0 , len(t)
        j = 0
        
        for i in range(len(s)):
            window[s[i]] = window.get(s[i], 0) + 1
            
            if s[i] in hashMap and window[s[i]] <= hashMap[s[i]]:
                have += 1
            
            while have == need:
                if i - j + 1 < minWindow:
                    minWindow = i - j + 1
                    minLeft = j
                    minRight = i

                window[s[j]] -= 1

                if s[j] in hashMap and window[s[j]] < hashMap[s[j]]:
                    have -= 1

                j += 1

        if minWindow != float('inf'):
            return s[minLeft:minRight+1]
        else:
            return ""

                


                    
                    

