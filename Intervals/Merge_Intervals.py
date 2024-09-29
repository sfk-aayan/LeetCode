class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        intSize = len(intervals)
        i = 0

        while i < intSize - 1:

            start, end = intervals[i][0], intervals[i][1]
            lStart, lEnd = intervals[i+1][0], intervals[i+1][1]

            if end >= lStart:
                intervals.pop(i+1)
                intervals[i][0], intervals[i][1] = start, max(lEnd, end)
                intSize -= 1

            else:
                i += 1

        return intervals        
        