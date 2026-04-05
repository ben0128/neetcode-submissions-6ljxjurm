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
        # { [value]: [ref] }
        nodeMap = {}
        for i in range(1, 101):
            nodeMap[i] = Node(i)
        # step 1 : bfs origin graph + hashMap
        tmp = deque([node])
        visited = set()

        while tmp:
            popNode = tmp.popleft()
            if popNode in visited:
                continue
            visited.add(popNode)
            for neigh in popNode.neighbors:
                nodeMap[popNode.val].neighbors.append(nodeMap[neigh.val])
                if neigh in visited:
                    continue
                tmp.append(neigh)

        return nodeMap[1]
