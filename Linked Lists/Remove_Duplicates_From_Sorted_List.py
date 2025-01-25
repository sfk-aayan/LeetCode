# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1000, head)

        prev, cur = dummy, head

        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next

        return dummy.next


#Another Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        dummy = ListNode(-1000)
        ptr = dummy

        while cur:
            if ptr.val == cur.val:
                cur = cur.next
                continue

            ptr.next = cur
            ptr = ptr.next
            cur = cur.next

        if ptr.next:
            ptr.next = None

        return dummy.next

        
        