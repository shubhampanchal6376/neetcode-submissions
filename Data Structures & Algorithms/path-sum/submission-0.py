# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = False
        s = 0 
        def fun(root,s,targetSum):
            nonlocal res
            if root is None:
                return 
            s += root.val
            if root.left is None and root.right is None:
                if s == targetSum:
                    res = True
                    return 
            fun(root.left,s,targetSum)
            fun(root.right,s,targetSum)
        fun(root,s,targetSum)
        return res