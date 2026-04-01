class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n-1 edges
        # no circle
        if n-1 != len(edges):
            return False
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

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
    

        if dfs(0, None):
            return len(visited) == n
        else:
            return False
        




        

        
        