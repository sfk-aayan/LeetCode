class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = defaultdict(list)

        for i in range(numCourses):
            mp[i]

        for go, to in prerequisites:
            mp[go].append(to)

        visit = set()
        nodeSet = set()

        def dfs(src):
            if src in visit:
                return False

            if src in nodeSet:
                return True

            visit.add(src)

            for n in mp[src]:
                if dfs(n) == False:
                    return False

            visit.remove(src)
            nodeSet.add(src)
            result.append(src)
            return True

        result = []

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return result