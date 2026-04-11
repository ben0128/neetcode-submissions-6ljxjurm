# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = [k]
        def inorder(n):
            if not n:
                return
            
            resL = inorder(n.left)
            if resL is not None:
                return resL
            count[0] -= 1
            if count[0] == 0:
                return n.val
            
            resR = inorder(n.right)
            if resR is not None:
                return resR
            return

        return inorder(root)