class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        numMap = defaultdict(list)
        for e, s in prerequisites:
            indegree[e] += 1
            numMap[s].append(e)

        tmp = deque([])
        count = 0
        # init 
        for i in range(numCourses):
            if indegree[i] == 0:
                count += 1
                tmp.append(i)

        while tmp:
            popN = tmp.popleft()
            for end in numMap[popN]:
                indegree[end] -= 1
                if indegree[end] == 0:
                    count += 1
                    tmp.append(end)
        return count == numCourses