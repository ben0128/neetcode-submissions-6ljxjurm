class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n-1 edges
        # no circle
        if n-1 != len(edges):
            return False
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def dfs(num, prev):
            visited.add(num)
            
            for node in graph[num]:
                if node == prev:
                    continue
                elif node in visited:
                    return False
                else:
                    if not dfs(node, num):
                        return False
            return True
    
        return dfs(0, None) and len(visited) == n


        

        
        