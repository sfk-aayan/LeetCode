# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur, prev = head, head
        llen = 0

        while cur:
            llen += 1
            cur = cur.next

        if llen == 1:
            return None

        dummy = ListNode(-1, head)
        rem = llen - n
        cur = dummy

        for _ in range(rem + 1):
            prev = cur
            cur = cur.next

        prev.next = cur.next if cur.next else None

        return dummy.next