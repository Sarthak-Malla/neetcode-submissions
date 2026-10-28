# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0
        h = head
        while h:
            h = h.next
            total += 1
        
        deletion = total - n
        prev = None
        h = head

        while deletion:
            prev = h
            h = h.next
            deletion -= 1
        
        if not prev:
            return h.next
        
        prev.next = h.next
        return head