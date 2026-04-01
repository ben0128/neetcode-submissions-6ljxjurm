# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(n):
            nonlocal k
            if not n:
                return False

            resL = dfs(n.left)
            if resL is not False:
                return resL

            k -= 1
            if k == 0:
                return n.val

            resR = dfs(n.right)
            if resR is not False:
                return resR
            return False

        return dfs(root)
        