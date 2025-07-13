class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i = 0
        j = len(costs) - 1
        heap1 = []
        heap2 = []
        ans = 0

        while k > 0:
            while len(heap1) < candidates and i <= j:
                heapq.heappush(heap1, costs[i])
                i += 1
            while len(heap2) < candidates and i <= j:
                heapq.heappush(heap2, costs[j])
                j -= 1

            val1 = heap1[0] if heap1 else float('inf')
            val2 = heap2[0] if heap2 else float('inf')

            if val1 <= val2:
                v = heapq.heappop(heap1)
                ans += v
            else:
                v = heapq.heappop(heap2)
                ans += v

            k -= 1

        return ans