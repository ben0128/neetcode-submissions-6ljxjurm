# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.tmpMax = -float('inf')

        def recursive(node):
            if not node:
                return 0
            
            resL = recursive(node.left)
            resR = recursive(node.right)
            v = node.val
            gainL = max(resL, 0)
            gainR = max(resR, 0)
            self.tmpMax = max(self.tmpMax, v+gainR+gainL)
            return v+max(gainR, gainL)
        recursive(root)
        return self.tmpMax