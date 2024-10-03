class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        size = len(points)
        i = 0

        while i < size - 1:
            start, end = points[i][0], points[i][1]
            newStart, newEnd = points[i+1][0], points[i+1][1]

            if end >= newStart and newEnd >= start:
                points.pop(i+1)
                points[i][0], points[i][1] = newStart, min(newEnd, end)
                size -= 1
            else:
                i += 1
        return size


        