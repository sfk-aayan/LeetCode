class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        if not words or not s:
            return []

        wordSize = len(words[0])
        strSize = len(s)
        maxLen = len(words) * wordSize 

        hashMap = {}

        for item in words:
            if item in hashMap:
                hashMap[item] += 1
            else:
                hashMap[item] = 1
            
        result = []

        for i in range(strSize - maxLen + 1):
            temp = {}

            for j in range(len(words)):
                start = i + j * wordSize
                substr = s[start: start + wordSize]

                if substr not in hashMap:
                    break
                
                temp[substr] = temp.get(substr, 0) + 1

                if temp[substr] > hashMap[substr]:
                    break

                
            if hashMap == temp:
                result.append(i)

        return result


