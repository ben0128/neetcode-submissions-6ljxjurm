class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for li in prerequisites:
            graph[li[1]].append(li[0])
        state = [0] * numCourses
    
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True

            state[node] = 1
            for el in graph[node]:
                if not dfs(el):
                    return False
            state[node] = 2
            return True

        for el in range(numCourses):
            if not dfs(el):
                return False
        return True