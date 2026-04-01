# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def dfs(node, idx):
            if node.left:
                temp = dfs(node.left, idx)
                if temp:
                    return temp

            idx[0] += 1
            if idx[0] == k:
                return node
            if node.right:
                temp = dfs(node.right, idx)
                if temp:
                    return temp
            return

        return dfs(root, [0]).val
        