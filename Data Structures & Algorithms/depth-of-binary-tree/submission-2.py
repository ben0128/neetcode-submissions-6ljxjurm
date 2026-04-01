# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node, deepth, ans):
            ans[0] = max(deepth, ans[0])

            if node.left:
                dfs(node.left, deepth+1, ans)
            if node.right:
                dfs(node.right, deepth+1, ans)
            return ans[0]
        return dfs(root, 1, [0])