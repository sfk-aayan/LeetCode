class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = defaultdict(list)

        for i in range(numCourses):
            mp[i]

        for go, to in prerequisites:
            mp[go].append(to)

        visit = set()
        nodeSet = set()

        def dfs(src):
            nodeSet.add(src)
            if src in visit:
                return False

            if mp[src] == []:
                return True

            visit.add(src)

            for n in mp[src]:
                if not dfs(n):
                    return False
            
            visit.remove(src)
            mp[src] = []
            return True

        for i in range(numCourses):
            if i not in nodeSet and not dfs(i):
                return False

        return True
        