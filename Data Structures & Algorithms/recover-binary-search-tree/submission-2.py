# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev = None
        g = 0 
        g11 = None
        g12 = None
        g21 = None
        g22 = None
        def fun(root):
            nonlocal prev,g,g11,g12,g21,g22
            if root is None:
                return
            fun(root.left)
            if prev is None:
                prev = root
            else:
                if root.val<prev.val:
                    if g == 0:
                        g11 = prev
                        g12 = root
                        g+=1
                    else:
                        g21 = prev
                        g22 = root
                        g+=1
                prev = root
            fun(root.right)
        fun(root)
        if g == 1:
            g11.val,g12.val = g12.val,g11.val
        else:
            g11.val,g22.val = g22.val,g11.val
        return 
        