# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        store = []
        while head:
            if head in store:
                return True
            store.append(head)
            head = head.next
        
        return False