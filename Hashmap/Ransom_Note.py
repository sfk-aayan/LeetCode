class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}

        for i in range(len(ransomNote)):
            hashMap[ransomNote[i]] = hashMap.get(ransomNote[i], 0) + 1

        for i in range(len(magazine)):
            if hashMap.get(magazine[i]) and hashMap[magazine[i]] > 0:
                hashMap[magazine[i]] -= 1
                if hashMap[magazine[i]] == 0:
                    del hashMap[magazine[i]]

        if not hashMap:
            return True
        return False
        
        