# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.idx = 0
        self.ans = None
        def dfs(node):
            if not node or self.ans:
                return
            
            dfs(node.left)

            self.idx += 1
            
            if self.idx == k:
                self.ans = node
            
            dfs(node.right)
            return
        

        dfs(root)

        return self.ans.val
        