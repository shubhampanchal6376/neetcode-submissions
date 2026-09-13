# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        def fun(root,m):
            nonlocal cnt
            if root is None:
                return 
            if root.val>=m:
                cnt+=1
                m = root.val
            fun(root.left,m)
            fun(root.right,m)
        fun(root,float('-inf'))
        return cnt