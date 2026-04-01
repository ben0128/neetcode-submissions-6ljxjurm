"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        # { oldNode: newNode }
        oldToNew = {}
        # 先掃一次創建含val的map

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            oldToNew[node] = Node(node.val)
            
            for neighbor in node.neighbors:
                oldToNew[node].neighbors.append(dfs(neighbor))
            return oldToNew[node]

        dfs(node)

        return oldToNew[node]

