class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0 for _ in range(numCourses)]
        
        nodeGraph = defaultdict(list)
        for end, start in prerequisites:
            nodeGraph[start].append(end)

        self.ans = []
        # 先檢查該點是否為灰色(-1), 如果是代表當前路徑有circle, return false, 遇到黑色(1) 就直接skip 代表走過了
        def dfs(entry):
            status = visited[entry]
            if status == -1:
                return False
            elif status == 1:
                return True
            else:
                visited[entry] = -1
                for nxtNode in nodeGraph[entry]:
                    if not dfs(nxtNode):
                        return False
            
            self.ans.append(entry)
            visited[entry] = 1
            return True
        for node in range(numCourses):
            if not dfs(node):
                return []
        return self.ans[::-1]