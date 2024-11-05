class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)

        for i, items in enumerate(equations):
            a, b = items
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def bfs(src, dst):
            if src not in adj or dst not in adj:
                return -1.00

            visited = set()
            q = deque()
            q.append((src, 1))

            while q:
                curr, wei = q.popleft()
                visited.add(curr)

                if curr == dst:
                    return wei

                for nei in adj[curr]:
                    n, w = nei

                    if n not in visited:
                        q.append((n, wei * w)) 

            return -1.00

        results = []

        for q in queries:
            src, dst = q
            results.append(bfs(src, dst))
        
        return results
        