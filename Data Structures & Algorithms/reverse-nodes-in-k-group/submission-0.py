# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        left = head
        flag = 0
        prevEnd = None
        while head:
            start = head
            for i in range(0, k):
                if not head:
                    if prevEnd:
                        prevEnd.next = start
                    break
                if i == k - 1:
                    print("here")
                    next_ = head.next
                    head.next = None
                    start, end = self.reverseList(start)
                    if not flag:
                        left = start
                        flag = 1
                    if prevEnd:
                        prevEnd.next = start
                    prevEnd = end
                    head = next_
                    continue

                head = head.next
        return left

    def reverseList(self, head):
        def reverse(curr, prev):
            if curr == None:
                return prev
            
            h = reverse(curr.next, curr)
            curr.next = prev

            return h
        
        h = reverse(head, None)
        tail = h
        while tail.next:
            tail = tail.next

        return h, tail