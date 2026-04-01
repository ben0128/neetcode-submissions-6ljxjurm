class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for x, y in points[:k]:
            sq = -pow(x**2+y**2, 0.5)
            heapq.heappush(hp, [sq, [x, y]])
        
        for x, y in points[k:]:
            sq = -pow(x**2+y**2, 0.5)
            if hp[0][0] < sq:
                heapq.heappop(hp)
                heapq.heappush(hp, [sq, [x, y]])
        return [el[1] for el in hp]