# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # root != None
        maxLen = [0]
        
        # dfs => memo every sub branch
        # todo:
        def dfs(n):
            if not n:
                return 0
            
            maxL, maxR = dfs(n.left), dfs(n.right)
            maxLen[0] = max(maxL+maxR, maxLen[0])

            return 1+max(maxL, maxR)

        dfs(root)
        return maxLen[0]
