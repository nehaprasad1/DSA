# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if (not head  or not head.next or not head.next.next):
            return
        fast , slow = head, head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        shead = slow.next
        slow.next = None
        curr = shead
        prev = None
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
            
        t1 = head
        t2= prev
        while t2:
            cat1 = t1.next
            cat2= t2.next
            t1.next = t2
            t2.next=cat1
            
            t1= cat1
            t2= cat2
            
        """
        Do not return anything, modify head in-place instead.
        """
        # see don't have to return anything 
        # we can divide the ll into two parts -> head - mid and mid+1 - tail using slow and fast technique 
        # second list need to be invested 
        #
        