class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = deque()
        stack.append(0)
        visited.add(0)

        while stack:
            index = stack.pop()

            for item in rooms[index]:
                if item not in visited:
                    visited.add(item)
                    stack.append(item)

        return len(visited) == len(rooms)




        return True