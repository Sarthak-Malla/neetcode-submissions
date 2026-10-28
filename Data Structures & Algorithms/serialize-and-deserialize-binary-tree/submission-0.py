# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    #Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        self.pre = []
        self.inorder = []
        def pre(root):
            if not root:
                return
            self.pre.append(str(root.val))
            pre(root.left)
            pre(root.right)
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.inorder.append(str(root.val))
            inorder(root.right)
        
        pre(root)
        inorder(root)

        return ",".join(self.pre) + " " + ",".join(self.inorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        [pre, ino] = data.split(" ")
        pre = pre.split(",")
        ino = ino.split(",")

        def construct(pre, ino):
            if not pre and not ino:
                return None
            
            if pre[0] == '':
                return None

            val = int(pre[0])
            root = TreeNode(val)
            mid = ino.index(str(val))

            root.left = construct(pre[1:mid+1], ino[:mid])
            root.right = construct(pre[mid+1:], ino[mid+1:])

            return root
        
        head = construct(pre, ino)

        return head
