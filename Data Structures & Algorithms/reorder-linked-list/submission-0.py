# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        self.flag = False
        def helper(top, curr, prev):
            if curr.next == None:
                return top
            
            top = helper(top, curr.next, curr)

            if top.next == None or top == curr:
                self.flag = True
                return top
                
            new_top = top
            if not self.flag:
                new_top = top.next
                top.next = curr.next
                curr.next.next = new_top
                curr.next = None

            return new_top
        
        helper(head, head, None)
