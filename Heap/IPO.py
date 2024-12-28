class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        items = []
        for i in range(len(profits)):
            items.append((capital[i], profits[i]))

        heapq.heapify(items)
        heap2 = []

        for i in range(k):
            
            while items and items[0][0] <= w:
                c, p = heapq.heappop(items)
                heapq.heappush(heap2, (-1 * p))

            if heap2:
                w += -1 * heapq.heappop(heap2)

        return w