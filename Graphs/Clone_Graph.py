"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        visited = set()
        stack = []

        stack.append(node)
        visited.add(node)
        hMap = {}

        while stack:
            curr = stack.pop()
            hMap[curr] = Node(curr.val)            

            for n in curr.neighbors:

                if n not in visited: 
                    stack.append(n)
                    visited.add(n)

        for old, new in hMap.items():
            
            for n in old.neighbors:
                new.neighbors.append(hMap[n])
                
        return hMap[node]