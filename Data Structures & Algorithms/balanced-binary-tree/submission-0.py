# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True

        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left) + 1
            right = helper(root.right) + 1

            if abs(right - left) > 1:
                self.flag = False
            
            return max(left, right)
        
        top = helper(root)
        return self.flag