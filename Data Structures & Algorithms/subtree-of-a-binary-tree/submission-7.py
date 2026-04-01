# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tmp = [root]
        subRootVal = subRoot.val
        def isSameTree(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2 or n1.val != n2.val:
                return False

            resL = isSameTree(n1.left, n2.left)
            resR = isSameTree(n1.right, n2.right)
            if not resL or not resR:
                return False
           
            return True
        # step 1: find the start_root of root
        while tmp:
            el = tmp.pop()
            if el.val == subRootVal and isSameTree(el, subRoot):
                return True
            if el.left:
                tmp.append(el.left)
            if el.right:
                tmp.append(el.right)
    
        return False


            