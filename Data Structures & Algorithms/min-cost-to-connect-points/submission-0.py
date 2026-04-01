class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()

        # (距離, idx)
        min_heap = [(0, 0)]

        res = 0
        while len(visited) < len(points):
            el = heapq.heappop(min_heap)
            if el[1] in visited:
                continue
            visited.add(el[1])
            res += el[0]
            for i in range(len(points)):
                if i not in visited:
                    heapq.heappush(min_heap, (abs(points[i][0]-points[el[1]][0]) + abs(points[i][1]-points[el[1]][1]), i))
        
        return res
