class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.map = {}
        self.left, self.right = ListNode(-1, -1), ListNode(-1, -1)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if self.map.get(key):
            newRight = self.map[key]

            self.delete(newRight)
            self.insert(newRight)

            return self.map[key].val

        return -1

    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = node
        node.prev = prv
        node.next = nxt
        nxt.prev = node

    def delete(self, node):    
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def put(self, key: int, value: int) -> None:
        if self.map.get(key):
            self.delete(self.map[key])
         
        self.map[key] = ListNode(key, value)
        self.insert(self.map[key])
        
        if len(self.map) > self.size:
            lft = self.left.next
            self.delete(lft)
            del self.map[lft.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)