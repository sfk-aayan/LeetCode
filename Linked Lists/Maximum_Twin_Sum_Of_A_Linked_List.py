# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        fast, slow = head, head
        maxLen = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        while head and prev:
            maxLen = max(maxLen, head.val+prev.val)
            head = head.next
            prev = prev.next

        return maxLen 
        