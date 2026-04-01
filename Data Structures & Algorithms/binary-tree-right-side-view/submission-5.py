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
            n = len(tmp)
            ans.append(tmp[-1].val)
            for _ in range(n):
                popEl = tmp.popleft()
                l, r = popEl.left, popEl.right
                if l:
                    tmp.append(l)
                if r:
                    tmp.append(r)
        return ans
