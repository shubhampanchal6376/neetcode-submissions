# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        a = []
        m = []
        asc = []
        t = root
        while t:
            asc.append(t)
            t = t.left
        def fun():
            if len(asc)==0:
                return None
            small = asc[-1]
            asc.pop()
            rightchild = small.right
            while rightchild:
                asc.append(rightchild)
                rightchild = rightchild.left
            return small
        while True:
            x = fun()
            if x is None:
                break
            a.append(x.val)
            m.append(x)
        b = []
        x = 0
        for i in a[::-1]:
            x += i
            b.append(x)
        b = b[::-1]
        for i in range(len(m)):
            m[i].val = b[i]
        return root
        