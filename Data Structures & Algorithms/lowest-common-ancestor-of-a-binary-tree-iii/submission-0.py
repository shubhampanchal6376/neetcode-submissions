"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a = []
        b = []
        while p:
            a.append(p)
            p = p.parent
        while q:
            b.append(q)
            q = q.parent
        for i in a :
            if i in b:
                return i