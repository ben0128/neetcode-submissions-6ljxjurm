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
            self.tmpMax = max(self.tmpMax, v+max(0, resL+resR, resL, resR))
            return node.val+max(resL, resR, 0)
        recursive(root)
        return self.tmpMax