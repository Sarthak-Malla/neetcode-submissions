# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr, prev):
            if curr == None:
                return prev
            
            h = reverse(curr.next, curr)
            curr.next = prev

            return h
        
        h = reverse(head, None)

        return h