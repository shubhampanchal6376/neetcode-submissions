# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = 0 
        a = 0 
        def fun(root,s):
            nonlocal a
            if root is None:
                return 
            s = s*10+root.val
            if root.left is None and root.right is None:
                a+=s
            fun(root.left,s)
            fun(root.right,s)
        fun(root,s)
        return a