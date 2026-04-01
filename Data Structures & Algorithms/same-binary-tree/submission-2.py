# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False

            resL = inorder(n1.left, n2.left)
            resR = inorder(n1.right, n2.right)

            if not resL or not resR or n1.val != n2.val:
                return False
            
            return True
            
        
        return inorder(p, q)