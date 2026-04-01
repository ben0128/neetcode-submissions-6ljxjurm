class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for node in edges:
            graph[node[0]].append(node[1])
            graph[node[1]].append(node[0])

        visited = set()
        def bfs(node, temp):
            while len(temp) > 0:
                poped = temp.popleft()
                for el in graph[poped]:
                    if el not in visited:
                        visited.add(el)
                        temp.append(el)

        ans = 0
        for num in range(n):
            if num not in visited:
                ans += 1
                visited.add(num)
                bfs(num, deque([num]))
        
        return ans

