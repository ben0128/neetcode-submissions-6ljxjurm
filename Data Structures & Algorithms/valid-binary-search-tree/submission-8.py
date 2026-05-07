# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        curr = root
        lastValue = -float('inf')
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            popEl = stack.pop()
            v = popEl.val
            if v <= lastValue:
                return False
            lastValue = v
            curr = popEl.right

        return True