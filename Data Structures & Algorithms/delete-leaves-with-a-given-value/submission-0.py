# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def fun(root):
            if root is None:
                return None
            root.left = fun(root.left)
            root.right = fun(root.right)
            if root.val == target and root.left is None and root.right is None:
                return None
            return root
        fun(root)
        return fun(root)

