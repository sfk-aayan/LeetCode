# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        llen = 0
        cur = head

        while cur:
            llen += 1
            cur = cur.next

        if llen == 1:
            return head 

        dummy = ListNode(-1, head)
        div = llen // k
        lPt = dummy
        cur = head
        divCt = 0


        while llen > 0:
            prev = None
            ct = 0

            if llen >= k:
                while ct < k and divCt <= div:
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp
                    ct += 1
                    
                divCt += 1
                temp = lPt.next
                lPt.next.next = cur
                lPt.next = prev 
                lPt = temp
                llen -= k
            else:
                llen -= 1

        return dummy.next
        