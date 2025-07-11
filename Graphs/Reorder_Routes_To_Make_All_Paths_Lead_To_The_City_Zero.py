class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(connections)):
            adj[connections[i][0]].append((connections[i][1], True))
            adj[connections[i][1]].append((connections[i][0], False))

        stack = deque()
        visited = set()
        ct = 0
        stack.append(0)
        visited.add(0)

        while stack:
            node = stack.pop()

            for neighbor, flag in adj[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
                    if flag:
                        ct += 1

        return ct