# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leng = 0 
        cur = head
        while cur:
            leng +=1
            cur = cur.next
        
        if n == leng:
            return head.next

        pre = head
        for _ in range(leng - n-1):            
            pre = pre.next

        pre.next =pre.next.next
        
        return head