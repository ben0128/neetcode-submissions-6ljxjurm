# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# preorder => mid, left, right
# inorder =>  left, mid, right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = defaultdict(int)
        n = len(preorder)
        for idx, num in enumerate(inorder):
            indexMap[num] = idx

        def recursive(l, preorderI, r):
            currRootIdx = preorderI[0]
            currRoot = TreeNode(preorder[currRootIdx])
            newRootIdx = indexMap[preorder[currRootIdx]]
            
            if newRootIdx-1 >= l:
                preorderI[0] += 1
                currRoot.left = recursive(l , preorderI, newRootIdx-1)
            if r >= newRootIdx+1:
                preorderI[0] += 1
                currRoot.right = recursive(newRootIdx+1, preorderI, r)
            return currRoot

        return recursive(0, [0], n-1)







