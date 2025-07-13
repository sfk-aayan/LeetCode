class SmallestInfiniteSet:

    def __init__(self):
        self.nums = []
        self.lookup = set()
        for i in range(1, 1001):
            self.nums.append(i)
            self.lookup.add(i)
        heapq.heapify(self.nums)

    def popSmallest(self) -> int:
        num = heapq.heappop(self.nums)
        self.lookup.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num not in self.lookup:
            heapq.heappush(self.nums, num)
            self.lookup.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)