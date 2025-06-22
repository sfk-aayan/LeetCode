class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0] * (len(gain) + 1)
        j = 1
        for item in range(len(gain)):
            res[j] = gain[item] + res[j-1]
            j += 1
        
        return max(res)