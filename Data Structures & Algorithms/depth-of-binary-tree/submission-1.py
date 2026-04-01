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
        ans = 0
        def dfs(node, deepth):
            nonlocal ans
            ans = max(deepth, ans)

            if node.left:
                dfs(node.left, deepth+1)
            if node.right:
                dfs(node.right, deepth+1)
            return
        dfs(root, 1)
        return ans