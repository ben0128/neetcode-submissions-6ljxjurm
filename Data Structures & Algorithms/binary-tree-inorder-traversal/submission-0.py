# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        path = []
        def helper(node):
            nonlocal path

            if node.left:
                helper(node.left)
            
            path.append(node.val)

            if node.right:
                helper(node.right)

        helper(root)
        return path