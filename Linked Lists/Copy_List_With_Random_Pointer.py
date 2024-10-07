"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hMap = {None : None}
        cur = head

        while cur:
            copy = Node(cur.val)
            hMap[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copy = hMap[cur]
            copy.next = hMap[cur.next]
            copy.random = hMap[cur.random]
            cur = cur.next
            
        return hMap[head]
        