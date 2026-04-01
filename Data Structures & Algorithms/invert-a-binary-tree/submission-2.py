# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tmp = deque([root])
        if not root:
            return root
        while tmp:
            popNode = tmp.popleft()
            popNode.left, popNode.right = popNode.right, popNode.left
            if popNode.left:
                tmp.append(popNode.left)
            if popNode.right:
                tmp.append(popNode.right)
        return root