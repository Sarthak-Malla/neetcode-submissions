# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        carry = 0
        h = head
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            s = a + b + carry
            carry = s // 10
            val = s % 10

            node = ListNode(val)
            head.next = node

            head = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry == 1:
            node = ListNode(1)
            head.next = node

        return h.next