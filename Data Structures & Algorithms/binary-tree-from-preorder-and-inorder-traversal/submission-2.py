# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {}
        n = len(inorder)
        for i in range(n):
            m[inorder[i]] = i
        idx = 0 
        def fun(preorder,low,high):
            nonlocal idx
            if low>high :
                return None
            node = TreeNode(preorder[idx])
            idx+=1
            index = m[node.val]
            node.left = fun(preorder,low,index-1)
            node.right = fun(preorder,index+1,high)
            return node
        return fun(preorder,0,n-1)