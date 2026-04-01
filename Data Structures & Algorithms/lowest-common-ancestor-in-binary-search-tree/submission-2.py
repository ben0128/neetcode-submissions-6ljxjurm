# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # {[treeNode]: [path]}
        hashMap = {}
        def dfs(node, path):
            if node.val == p.val:
                hashMap[p] = path.copy()
                if len(hashMap.keys()) == 2:
                    return True
            elif node.val == q.val:
                hashMap[q] = path.copy()
                if len(hashMap.keys()) == 2:
                    return True
            
            if node.left:
                path.append(node.left)
                resL = dfs(node.left, path)
                if resL:
                    return
                path.pop()
            if node.right:
                path.append(node.right)
                resR = dfs(node.right, path)
                if resR:
                    return
                path.pop()
            return False

        dfs(root, [root])
        ans = None
        for idx in range(min(len(hashMap[p]), len(hashMap[q]))):
            if hashMap[p][idx] == hashMap[q][idx]:
                ans = hashMap[p][idx]
            else:
                return ans
        return ans

