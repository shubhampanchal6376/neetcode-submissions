# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def fun(root,p,q):
            nonlocal ans
            if root is None:
                return 0
            l = fun(root.left,p,q)
            r = fun(root.right,p,q)
            s = 0 
            if root.val == p.val or root.val == q.val:
                s=1
            total = s+l+r
            if total == 2 and ans == None:
                ans = root
            return total
        fun(root,p,q)
        return ans 