class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairArr = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        pairArr.sort(key=lambda x: x[1], reverse=True)

        heap = []
        s = 0
        ans = 0

        for i in range(k):
            s += pairArr[i][0]
            heapq.heappush(heap, pairArr[i][0])

        ans = s * pairArr[k-1][1]

        for i in range(k, len(pairArr)):
            if pairArr[i][0] > heap[0]:
                s -= heap[0]
                heapq.heappop(heap)
                heapq.heappush(heap, pairArr[i][0])
                s += pairArr[i][0]

                ans = max(ans, pairArr[i][1] * s)
        return ans