# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            root = list1
            list1 = list1.next
        else:
            root = list2
            list2 = list2.next
        it = root
        while list1 and list2:
            # compare
            if list1.val <= list2.val:
                it.next = list1
                list1 = list1.next
            else:
                it.next = list2
                list2 = list2.next
            it = it.next
        
        if list1:
            it.next = list1
        elif list2:
            it.next = list2

        return root