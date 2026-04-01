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
        ans = [root.val]
        tmp = deque([root])
        while tmp:
            l = len(tmp)
            for i in range(l):
                popedEl = deque.popleft(tmp)
                if popedEl.left:
                    tmp.append(popedEl.left)
                if popedEl.right:
                    tmp.append(popedEl.right)
            if tmp:
                ans.append(tmp[-1].val)

        return ans