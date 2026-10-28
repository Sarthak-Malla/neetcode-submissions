# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                mergedList.append(self.mergeList(l1, l2))
            
            lists = mergedList
            
        return lists[0]


    def mergeList(self, list1, list2):
        start = ListNode()
        head = start
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                start.next = list1
                start = start.next
                list1 = list1.next
            else:
                start.next = list2
                start = start.next
                list2 = list2.next
        
        if list1 != None:
            start.next = list1
        
        if list2 != None:
            start.next = list2
        
        return head.next