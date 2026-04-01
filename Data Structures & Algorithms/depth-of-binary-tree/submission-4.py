# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lv = 0
        
        tmp = deque([root])
        while tmp:
            lv += 1
            n = len(tmp)

            for _ in range(n):
                popEl = tmp.popleft()
                l, r = popEl.left, popEl.right
                if l:
                    tmp.append(l)
                if r:
                    tmp.append(r)
        return lv