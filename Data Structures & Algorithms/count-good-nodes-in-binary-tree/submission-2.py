# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # dfs function return
        def dfs(n: TreeNode, tmpMax) -> int:
            if not n:
                return 0
            v = n.val
            tmpCount = 1 if v >= tmpMax else 0
            tmpMax = max(tmpMax, v)
            tmpCount += dfs(n.left, tmpMax)
            tmpCount += dfs(n.right, tmpMax)
            
            return tmpCount
        return dfs(root, -101)

        