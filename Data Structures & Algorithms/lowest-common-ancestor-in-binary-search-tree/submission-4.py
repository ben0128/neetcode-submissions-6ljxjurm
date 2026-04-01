# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        need = [p.val, q.val]
        
        def dfs(n):
            if not n:
                return None
            if n.val in need:
                return n
            resL = dfs(n.left)
            resR = dfs(n.right)          
            if resR and resL:
                return n
            if resR:
                return resR
            if resL:
                return resL
            return None
        
        return dfs(root)