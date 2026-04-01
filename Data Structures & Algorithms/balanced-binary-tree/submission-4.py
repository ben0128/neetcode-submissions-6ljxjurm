# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # [bool, maxLen]
        def checkBalance(n):
            if not n:
                return [True, 0]
            
            [resL, maxL], [resR, maxR] = checkBalance(n.left), checkBalance(n.right)
            if not resL or not resR or abs(maxL-maxR) > 1:
                return [False, 0]
            
            return [True, 1+max(maxL, maxR)]
        
        return checkBalance(root)[0]
        