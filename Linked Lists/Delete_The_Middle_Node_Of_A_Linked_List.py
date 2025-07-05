# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        lenn = 0
        while cur:
            lenn += 1
            cur = cur.next
        
        middle = lenn // 2

        lenn = 0
        dummy = ListNode(-1, next = head)
        cur = dummy

        while cur:
            if lenn == middle:
                cur.next = cur.next.next
                break
            lenn += 1    
            cur = cur.next
        
        return dummy.next