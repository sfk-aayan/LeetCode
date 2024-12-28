class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        heapq.heappush(heap, (nums1[0]+nums2[0], (0, 0)))
        visited = set((0, 0))
        res = []

        for i in range(k):
            _, indices = heappop(heap)
            i1, i2 = indices
            res.append((nums1[i1], nums2[i2]))

            i1_next = i1 + 1
            i2_next = i2 + 1

            if i2_next < len(nums2) and (i1, i2_next) not in visited:
                heapq.heappush(heap, (nums1[i1]+nums2[i2_next], (i1, i2_next)))
                visited.add((i1, i2_next))

            if i1_next < len(nums1) and (i1_next, i2) not in visited:
                heapq.heappush(heap, (nums1[i1_next]+nums2[i2], (i1_next, i2)))
                visited.add((i1_next, i2))
    
        return res

        