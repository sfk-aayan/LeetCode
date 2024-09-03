class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        words2 = []

        for item in words:
            if item != "":
                words2.append(item)
        
        return len(words2[len(words2) - 1])         
        