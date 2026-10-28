"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def helper(head):
            if not head:
                return None

            new_node = Node(head.val, None, None)
            ori_next = head.next

            head.next = new_node

            new_next = helper(ori_next)

            new_node.next = new_next
            new_node.random = head.random.next if head.random else None

            return new_node
        
        return helper(head)

