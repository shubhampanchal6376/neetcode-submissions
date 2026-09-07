# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        ans = []
        def fun(root):
            if root is None:
                return 
            fun(root.left)
            ans.append(root)
            fun(root.right)
        fun(root)
        g = 0
        g11 = 0
        g12 = 0
        g21 = 0
        g22 = 0
        for i in range(len(ans)-1):
            if ans[i].val>ans[i+1].val:
                if g == 0:
                    g11 = ans[i]
                    g12 = ans[i+1]
                    g+=1
                else:
                    g21 = ans[i]
                    g22 = ans[i+1]
                    g+=1
        if g == 1:
            g11.val , g12.val = g12.val , g11.val
        else:
            g11.val,g22.val = g22.val,g11.val
        return 
        

