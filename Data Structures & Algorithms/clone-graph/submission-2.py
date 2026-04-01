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
        oldToNew[node] = Node(node.val)
        temp = [node]

        while len(temp) > 0:
            poped = temp.pop(0)
            for neighbor in poped.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    temp.append(neighbor)
                oldToNew[poped].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]

