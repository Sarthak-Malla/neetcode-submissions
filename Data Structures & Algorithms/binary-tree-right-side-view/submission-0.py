# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.hash = {}

        def helper(root, depth):
            if not root:
                return
            
            helper(root.left, depth + 1)
            if not self.hash.get(depth):
                self.hash[depth] = []
            self.hash[depth].append(root.val)
            helper(root.right, depth + 1)

        helper(root, 0)

        ans = []
        for key in sorted(self.hash.keys()):
            ans.append(self.hash[key])
        
        res = [x[-1] for x in ans]

        return res