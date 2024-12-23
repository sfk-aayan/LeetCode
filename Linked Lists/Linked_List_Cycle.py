# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        
        slowPt = head
        fastPt = head

        while fastPt != None and fastPt.next != None:
            slowPt = slowPt.next
            fastPt = fastPt.next.next

            if slowPt == fastPt:
                return True

        return False 