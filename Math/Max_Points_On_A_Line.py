class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0

        for i in range(len(points)):
            gradCounter = {}
            for j in range(i+1, len(points)):
                nom = points[j][1] - points[i][1]
                denom = points[j][0] - points[i][0]
                if denom == 0:
                    g = float('inf')
                else:
                    g =  nom / denom
                
                gradCounter[g] = gradCounter.get(g, 0) + 1
                res = max(gradCounter[g], res)
        return res + 1
        