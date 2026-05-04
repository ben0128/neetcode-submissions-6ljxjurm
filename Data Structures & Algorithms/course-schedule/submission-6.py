class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        numMap = defaultdict(list)
        for e, s in prerequisites:
            indegree[e] += 1
            numMap[s].append(e)

        visited = set()
        tmp = deque([])
        # init 
        for i in range(numCourses):
            if indegree[i] == 0:
                tmp.append(i)

        while tmp:
            n = len(tmp)
            for _ in range(n):
                popN = tmp.popleft()
                visited.add(popN)
                
                for end in numMap[popN]:
                    if end in visited:
                        continue
                    indegree[end] -= 1
                    if indegree[end] == 0:
                        tmp.append(end)
        for count in indegree:
            if count != 0:
                return False
        return True