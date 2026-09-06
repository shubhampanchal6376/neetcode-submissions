# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        ans = False
        if root is None:
            return True
        q.append(root)
        while q:
            x = q[0]
            q.popleft()
            if x == None:
                ans = True
            else:
                if ans:
                    return False
                q.append(x.left)
                q.append(x.right)
        return ans
        
