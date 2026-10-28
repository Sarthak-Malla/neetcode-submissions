# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        def helper(head, prev):
            if not head.next:
                head.next = prev
                return head
            
            n = head.next
            head.next = prev
            return helper(n, head)
        
        return helper(head, None)