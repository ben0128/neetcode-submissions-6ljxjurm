# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # node.val == target and not node.left and not node.right
        def dfs(n):
            if not n:
                return False
            
            if dfs(n.left):
                n.left = None

            if n.val == target and not n.left and not n.right:
                return True

            if dfs(n.right):
                n.right = None

            return True if n.val == target and not n.left and not n.right else False
        res = dfs(root)
        return None if res else root