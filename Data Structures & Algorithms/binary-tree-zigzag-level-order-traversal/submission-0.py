# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        if root:
            q.append(root)
        lr = 1
        while q:
            l = len(q)
            temp = [0]*l
            f = 0 
            r = l-1
            while l>0:
                x = q[0]
                q.popleft()
                if lr == 1:
                    temp[f]=x.val
                    f+=1
                else:
                    temp[r] = x.val
                    r-=1
                l-=1
                if x.left is not None:
                    q.append(x.left)
                if x.right is not None:
                    q.append(x.right)
            ans.append(temp)
            lr = 1- lr
        return ans
                                            
