# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def Smallest(root):
            if root is None:
                return 
            Smallest(root.left)
            ans.append(root.val)
            Smallest(root.right)
        Smallest(root)
        return ans[k-1]