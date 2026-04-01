class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for el in prerequisites:
            graph[el[1]].append(el[0])
                

        state = [0] * numCourses 
        # 0 沒走過
        # 1 正在走
        # 2 走完了
        print(graph)
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

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
            
