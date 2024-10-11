# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-1000, head)
        cur = dummy
        dummy2 = ListNode(-2000)
        ptr2 = dummy2

        while cur and cur.next:

            if cur.next and cur.next.val >= x:
                newCur = cur

                while newCur.next and newCur.next.val >= x:
                    newCur = newCur.next
                    ptr2.next = ListNode(newCur.val)
                    ptr2 = ptr2.next
                cur.next = newCur.next
                cur = cur.next
            else:
                cur = cur.next

        ptr1 = dummy
        
        while ptr1.next:
            ptr1 = ptr1.next

        ptr1.next = dummy2.next

        return dummy.next