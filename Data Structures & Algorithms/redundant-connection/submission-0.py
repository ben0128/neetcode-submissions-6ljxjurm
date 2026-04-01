class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 尋找環,並return環中在input最後一條路
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        print(graph)
        path = set()
        def dfs(node, parent):
            if node in path:
                return True
            
            path.add(node)
            for point in graph[node]:
                if point != parent:
                    if dfs(point, node):
                        return True
            path.remove(node)

        dfs(edges[0][0], None)
        for x, y in edges[::-1]:
            if x in path and y in path:
                return [x,y]
