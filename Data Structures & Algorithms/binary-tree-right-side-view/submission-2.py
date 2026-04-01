# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        tmp = deque([root])
        while tmp:
            l = len(tmp)
            for i in range(l):
                popedEl = deque.popleft(tmp)
                if i == l-1:
                    ans.append(popedEl.val)
                if popedEl.left:
                    tmp.append(popedEl.left)
                if popedEl.right:
                    tmp.append(popedEl.right)
        return ans