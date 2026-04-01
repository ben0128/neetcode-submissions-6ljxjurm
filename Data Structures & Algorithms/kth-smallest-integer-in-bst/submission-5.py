# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [k]

        def inorder(n):
            if not n:
                return None
            resL = inorder(n.left)
            if resL:
                return resL
            
            count[0] -= 1
            if count[0] == 0:
                return n
            
            resR = inorder(n.right)
            if resR:
                return resR
            
            return None
        return inorder(root).val
        