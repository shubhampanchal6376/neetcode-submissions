# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = [] 
        def fun(root):
            if root is None:
                return 
            fun(root.left)
            ans.append(root.val)
            fun(root.right)
        fun(root)
        a = 0
        for i in ans:
            if i>=low and i<=high:
                a+=i
        return a
