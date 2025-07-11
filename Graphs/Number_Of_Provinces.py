class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    adj[i].append(j)
        
        stack = deque()
        visited = set()
        ct = 0
        for i in range(len(isConnected)):
            if i not in visited:
                stack.append(i)
                visited.add(i)

                while stack:
                    node = stack.pop()

                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                ct += 1

        return ct