# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        pt1 = l1
        pt2 = l2
        carry = 0

        while pt1 != None and pt2 != None:
            curr = pt1.val + pt2.val + carry

            if curr > 9:
                carry = curr // 10
                curr = curr % 10
            else:
                carry = 0
                        
            pt1.val = curr
            pt2.val = curr
            pt1 = pt1.next
            pt2 = pt2.next

        check = pt2 if pt1 == None else pt1
        ans = last = l1 if check == pt1 else l2
        
        while check != None:
            curr = check.val + carry
            
            if curr > 9:
                carry = curr // 10
                curr = curr % 10
            else:
                carry = 0
            
            check.val = curr
            check = check.next

        if carry > 0:
            newNode = ListNode(carry)
            while last.next != None:
                last = last.next

            last.next = newNode    

        return ans
        