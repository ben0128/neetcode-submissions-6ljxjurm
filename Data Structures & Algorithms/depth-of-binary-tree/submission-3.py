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
        
        tmp = deque([root])
        ans = 0

        while tmp:  
            ans += 1
            l = len(tmp)
            for _ in range(l):
                popEl = tmp.popleft()
                if popEl.left:
                    tmp.append(popEl.left)
                if popEl.right:
                    tmp.append(popEl.right)
        return ans
            