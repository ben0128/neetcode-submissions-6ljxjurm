# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        
        def dfs(node, deepth):
            if deepth == len(ans):
                ans.append(node.val)
            
            if node.right:
                dfs(node.right, deepth+1)
            if node.left:
                dfs(node.left, deepth+1)
            return
        dfs(root, 0)
        return ans