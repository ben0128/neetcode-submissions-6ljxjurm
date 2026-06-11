# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        # let p.val > q.val
        if p.val < q.val:
            p, q = q, p
        pval, qval = p.val, q.val

        while curr:
            currVal = curr.val
            if qval <= currVal <= pval:
                return curr
            
            if currVal < pval:
                curr = curr.right
            else:
                curr = curr.left