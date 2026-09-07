# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def fun(root):
            if root is None:
                return 
            fun(root.left)
            ans.append(root.val)
            fun(root.right)
        fun(root)
        for i in range(1,len(ans)):
            if ans[i-1]>=ans[i]:
                return False
        return True