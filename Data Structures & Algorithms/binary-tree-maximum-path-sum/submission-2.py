# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum = [root.val]
        minNum = -float('inf')
        def travesal(n):
            if not n:
                return minNum
            currVal = n.val
            resL = travesal(n.left)
            resR = travesal(n.right)
            currMax = max(currVal, currVal+resR, currVal+resL)
            maxSum[0] = max(maxSum[0], currMax, resR+currVal+resL)

            return currMax
        
        travesal(root)
        return maxSum[0]