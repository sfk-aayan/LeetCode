# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        llen = 0

        cur = head

        while cur:
            llen += 1
            cur = cur.next

        div = k % llen

        if div == 0:
            return head

        cur = head
        prev = cur
        for _ in range(llen - div):
            prev = cur
            cur = cur.next

        while cur.next:
            cur = cur.next

        newHead = prev.next
        prev.next = None
        cur.next = head

        return newHead



        return head.next
        