# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_ = root.val

        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left) + root.val
            right = helper(root.right) + root.val

            self.max_ = max(self.max_, left + right - root.val)
            self.max_ = max(self.max_, root.val)

            return max(left, right)
        
        top = helper(root)

        return max(top, self.max_)