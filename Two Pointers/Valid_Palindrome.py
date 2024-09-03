class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        
        i = 0
        j = len(s) - 1

        if s == "":
            return True

        while i < len(s) and j >= 0:
            if s[i] != s[j]:
                return False   

            i += 1 
            j -= 1 

        return True


        