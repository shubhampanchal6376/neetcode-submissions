# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        m = {}
        n = len(inorder)
        for i in range(n):
            m[inorder[i]] = i
        idx = n-1 
        def fun(posteorder,low,high):
            nonlocal idx
            if low>high :
                return None
            node = TreeNode(postorder[idx])
            idx-=1
            index = m[node.val]
            node.right = fun(postorder,index+1,high)
            node.left = fun(postorder,low,index-1)
            return node
        return fun(postorder,0,n-1)