# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # [res, [tmpMin, tmpMax]]
        defaultCandi = [float('inf'), -float('inf')]
        def dfs(n):
            if not n:
                return [True, defaultCandi]

            [isValidL, [minL, maxL]] = dfs(n.left)
            [isValidR, [minR, maxR]] = dfs(n.right)
            if not isValidL or not isValidR or not (maxL < n.val < minR):
                return [False, defaultCandi]

            return [True, [min(minL, n.val), max(maxR, n.val)]]
            
        return dfs(root)[0]