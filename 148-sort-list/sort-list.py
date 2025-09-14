# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  head is None or head.next is None:
            return head
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        curr = head
        for val in arr:
            curr.val = val
            curr = curr.next
        return head

        
        '''
        # Get the middle of the list. then split the list. Make  them into left and right list. Recursive call on the main function on left and right  
        
        if  head is None or head.next is None:
            return head
        
        mid = self.get_mid(head)
        next_to_mid = mid.next
        mid.next = None

        left = self.sortList(head)
        right =self.sortList(next_to_mid)
        
        return self.merge(left,right)
        
    def get_mid(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        
        if left.val < right.val:
            result = left
            result.next = self.merge(left.next,right)
        else:
            result = right
            result.next = self.merge(left,result.next)
        return result 
        '''

        
