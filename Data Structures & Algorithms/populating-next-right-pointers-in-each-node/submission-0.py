"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        ans = []
        q = deque()
        if root:
            q.append(root)
        while q:
            l = len(q)
            temp = []
            while l>0:
                x = q[0]
                q.popleft()
                temp.append(x)
                if x.left!=None:
                    q.append(x.left)
                if x.right!=None:
                    q.append(x.right)
                l-=1
            ans+=temp+[None]
        for i in range(len(ans)-1):
            if ans[i] is None:
                continue
            else:
                ans[i].next = ans[i+1]
        return root

















        