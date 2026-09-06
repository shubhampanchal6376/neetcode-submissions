# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        a = 0
        q = deque()
        if root:
            q.append(root)
        while q:
            l = len(q)
            temp = []
            while l>0:
                x = q[0]
                q.popleft()
                temp.append(x.val)
                if x.left != None:
                    q.append(x.left)
                if x.right != None:
                    q.append(x.right)
                l-=1
            a+=1
        return a