# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_ = float("-infinity")

        def helper(root):
            if not root:
                return -1
            
            left = helper(root.left) + 1
            right = helper(root.right) + 1

            self.max_ = max(self.max_, left + right)

            return max(left, right)
        
        top = helper(root)

        return max(top, self.max_)
        