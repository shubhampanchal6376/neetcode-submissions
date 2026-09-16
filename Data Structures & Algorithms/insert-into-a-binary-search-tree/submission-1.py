# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        if root is None:
            return TreeNode(val)
        def fun(root):
            if root.val > val:
                if root.left is None:
                    x = TreeNode(val)
                    root.left = x
                else:
                    fun(root.left)
            else:
                if root.right is None:
                    y = TreeNode(val)
                    root.right = y
                else:
                    fun(root.right)
        fun(root)
        return curr
        