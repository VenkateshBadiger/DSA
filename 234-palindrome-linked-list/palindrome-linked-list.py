# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Make a list of values and compare with its reverse 
        values = []
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next

        return values == values[::-1]
        
        """
        # Find the middle first. Reverse the elements after middle and then check from the start if the values are same on left and right.
        if head is None or head.next is None:
            return True
        
        slow = head 
        fast=  head 

        while fast is not None and fast.next is not None:
            slow= slow.next
            fast =  fast.next.next
        
        
        prev = None
        cur = slow         
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        left, right = head, prev
        while right:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        return True
        """