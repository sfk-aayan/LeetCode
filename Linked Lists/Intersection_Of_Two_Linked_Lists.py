# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ctr1 = headA
        ctr2 = headB

        lenA = 0
        lenB = 0
        while ctr1:
            lenA += 1
            ctr1 = ctr1.next

        while ctr2:
            lenB += 1
            ctr2 = ctr2.next
        
        ctr1 = headA
        ctr2 = headB
        flag = None

        if lenA > lenB:
            diff = lenA - lenB

            for i in range(diff):
                ctr1 = ctr1.next

            while ctr1 and ctr2:
                if ctr1 == ctr2:
                    flag = ctr1
                    break
                
                ctr1 = ctr1.next
                ctr2 = ctr2.next

        else:
            diff = lenB - lenA

            for i in range(diff):
                ctr2 = ctr2.next

            while ctr1 and ctr2:
                if ctr1 == ctr2:
                    flag = ctr2
                    break
                
                ctr1 = ctr1.next
                ctr2 = ctr2.next

        return flag
                