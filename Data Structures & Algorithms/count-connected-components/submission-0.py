class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for node in edges:
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])

        print(graph)


        visited = set()
        def dfs(node):
            visited.add(node)
            for el in graph[node]: 
                if el not in visited:
                    dfs(el)


        ans = 0
        for num in range(n):
            if num not in visited:
                ans += 1
                dfs(num)
        
        return ans

