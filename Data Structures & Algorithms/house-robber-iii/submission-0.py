# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def inorder(n):
            if not n:
                return (0, 0)
            
            # 3, 6
            resL1, resL2 = inorder(n.left)
            # 5, 0
            resR1, resR2 = inorder(n.right)
            
            #(偷當前的節點的最大值, 不偷當前節點的最大值) 
            return (n.val+resL2+resR2, max(resL1, resL2)+max(resR1, resR2))

        res = inorder(root)

        return max(res[0], res[1])