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
        tmp = deque([root])
        ans = []
        while tmp:
            n = len(tmp)
            tmpAns = []
            for _ in range(n):
                popEl = tmp.popleft()
                tmpAns.append(popEl.val)
                l, r = popEl.left, popEl.right
                if l:
                    tmp.append(l)
                if r:
                    tmp.append(r)
            if tmpAns:
                ans.append(tmpAns)
        return ans
            