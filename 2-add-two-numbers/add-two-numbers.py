# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = 0
        b = 0
        mult = 1
        cur = l1
        while cur:
            a = a + cur.val*mult
            mult *= 10 
            cur = cur.next
        mult = 1
        cur = l2
        while cur:
            b = b + cur.val*mult
            mult *= 10
            cur = cur.next

        c = a + b
        
        new = ListNode(0)
        cur = new
        if c == 0:
            return ListNode(0)
        while c > 0:
            cur.next = ListNode(c % 10)
            c = c // 10
            cur = cur.next

        return new.next