# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small, big = p.val, q.val
        if small > big:
            small, big = big, small
        def lca(node):
            if small <= node.val <= big:
                return node
            
            if node.val > big:
                return lca(node.left)
            if node.val < small:
                return lca(node.right)

        return lca(root)