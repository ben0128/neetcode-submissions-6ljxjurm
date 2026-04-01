class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        count = 0
        graph = defaultdict(list)
        visited = set()
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for sideNode in graph[node]:
                dfs(sideNode)
            return

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count


        