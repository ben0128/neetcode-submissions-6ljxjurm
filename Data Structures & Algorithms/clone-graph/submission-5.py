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
        nodeMap = {node.val: Node(node.val)}
        # step 1 : bfs origin graph + hashMap
        tmp = deque([node])
        visited = set()

        while tmp:
            popNode = tmp.popleft()
            if popNode in visited:
                continue
            visited.add(popNode)
            for neigh in popNode.neighbors:
                vp, vn = popNode.val, neigh.val
                if vn not in nodeMap:
                    nodeMap[vn] = Node(vn)
                nodeMap[vp].neighbors.append(nodeMap[vn])
                if neigh in visited:
                    continue
                
                tmp.append(neigh)

        return nodeMap[node.val]
