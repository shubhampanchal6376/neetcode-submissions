# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        if root :
            q.append(root)
        while q:
            l = len(q)
            temp = [] 
            while l:
                x = q[0]
                q.popleft()
                temp.append(x.val)
                if x.left!=None:
                    q.append(x.left)
                if x.right!=None:
                    q.append(x.right)
                l-=1
            ans.append(temp)
        return ans