class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intSize = len(intervals)
        if intSize == 0:
            return [newInterval]
        i = 0
        result = []

        for i in range(intSize):
            start, end = intervals[i][0], intervals[i][1]

            if end < newInterval[0]:
                result.append([start, end])

            elif newInterval[1] < start:
                result.append(newInterval)
                newInterval = [start, end]
                
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
                
        result.append(newInterval)

        return result
        