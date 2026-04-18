# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def postorder(node):
            if node is None or node == p or node == q:
                return node
            
            resL = postorder(node.left)
            resR = postorder(node.right)
            if resL and resR:
                return node

            return resR or resL

        return postorder(root)