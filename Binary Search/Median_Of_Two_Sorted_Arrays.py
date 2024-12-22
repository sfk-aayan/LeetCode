class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        if len2 < len1:
            return self.findMedianSortedArrays(nums2, nums1)

        partition = (len1 + len2 + 1) // 2
        total = len1 + len2

        low = 0
        high = len1

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = partition - mid1

            l1 = l2 = float('-inf')
            r1 = r2 = float('inf')

            if mid1 < len1:
                r1 = nums1[mid1]
            if mid2 < len2:
                r2 = nums2[mid2]

            if mid1 - 1 >= 0:
                l1 = nums1[mid1-1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2-1]

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)

            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return 0

        