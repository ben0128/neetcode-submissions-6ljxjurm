# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        numMap = {num: idx for idx, num in enumerate(inorder)}
        
        def dfs(preL, preR, inL, inR):
            if preL > preR or inL > inR:
                return None
            root = TreeNode(preorder[preL])
            mid = numMap[root.val]
            l = mid - inL
            # root.left = self.buildTree(preorder[1:1+mid], inorder[:mid])
            root.left = dfs(preL+1, (l+preL), inL, (mid-1))
            # root.right = self.buildTree(preorder[1+mid:], inorder[mid+1:])
            root.right = dfs((preL+l+1), preR, (mid+1), inR)
            return root

        return dfs(0, (len(preorder)-1), 0, (len(inorder)-1))




