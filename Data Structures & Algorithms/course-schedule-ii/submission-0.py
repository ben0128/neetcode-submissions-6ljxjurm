class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # graph
        graph = defaultdict(list)
        for li in prerequisites:
            graph[li[1]].append(li[0])
        print(graph)
        
        visited = [0] * numCourses
        res = list()

        def dfs(node):
            # 正在走
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            
            visited[node] = 1

            for el in graph[node]:
                if not dfs(el):
                    return False
            visited[node] = 2
            res.append(node)
            return True

        for idx in range(numCourses):
            if not dfs(idx):
                return []
        return res[::-1]