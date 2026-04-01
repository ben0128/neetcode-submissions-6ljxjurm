# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        temp = [root]
        ans = []
        while len(temp) > 0:
            n = len(temp)
            li = []
            for idx in range(n):
                el = temp.pop(0)
                li.append(el.val)
                if el.left:
                    temp.append(el.left)
                if el.right:
                    temp.append(el.right)
            ans.append(li)
        return ans
            