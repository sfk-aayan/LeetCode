class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        minLen = len(self.minHeap)
        maxLen = len(self.maxHeap)

        if abs(maxLen - minLen) > 1:
            val = -heappop(self.maxHeap)
            heappush(self.minHeap, val)
        
        if self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            temp = -heappop(self.maxHeap)
            heappush(self.maxHeap, -self.minHeap[0]) 
            heappop(self.minHeap)
            heappush(self.minHeap, temp)

    def findMedian(self) -> float:
        minLen = len(self.minHeap)
        maxLen = len(self.maxHeap)

        if (minLen + maxLen) % 2 == 0:
            left = -self.maxHeap[0]
            right = self.minHeap[0]
            return (left + right) / 2
        else:
            return -self.maxHeap[0] if maxLen > minLen else self.minHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()