# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def helper(root, m):
            if not root:
                return
            
            helper(root.left, max(m, root.val))
            if root.val >= m:
                self.ans += 1
            helper(root.right, max(m, root.val))

        
        helper(root, float('-infinity'))
        return self.ans