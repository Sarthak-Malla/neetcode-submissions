# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = float('-infinity')

        def helper(root, curr, depth):
            if not root:
                depth = max(depth, curr)
                return depth
            
            depth = helper(root.left, curr + 1, depth)
            depth = helper(root.right, curr + 1, depth)
        
            return depth
        
        depth = helper(root, 0, depth)

        return depth