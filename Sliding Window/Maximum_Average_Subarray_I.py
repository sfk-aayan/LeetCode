class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]/1
        prev = 0
        nxt = 0
        maxA = float('-inf')
        ct = 0

        while nxt < len(nums) and nxt - prev + 1 < k:
            ct += nums[nxt]
            nxt += 1

        ct += nums[nxt]
        maxA = max(maxA, ct/k)
        
        while nxt < len(nums) - 1:
            ct -= nums[prev]
            prev += 1
            nxt += 1  
            ct += nums[nxt]
            maxA = max(maxA, ct/k)    

        return maxA
            