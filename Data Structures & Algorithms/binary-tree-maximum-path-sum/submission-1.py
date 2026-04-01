# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -float('inf')

        def dfs(node, total):
            nonlocal maxSum
            if not node:
                return 0

            leftMax = dfs(node.left, total+node.val)
            rightMax = dfs(node.right, total+node.val)
            tempMax = max(leftMax+node.val, rightMax+node.val, node.val+leftMax+rightMax, node.val)
            maxSum = max(tempMax, maxSum)
            return max(leftMax+node.val, rightMax+node.val, node.val)

        dfs(root, root.val)
        return maxSum