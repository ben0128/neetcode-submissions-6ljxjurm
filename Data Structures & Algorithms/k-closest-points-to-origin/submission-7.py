
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxH = []
        for i, [x,y] in enumerate(points):
            dis = x ** 2 + y ** 2
            heapq.heappush(maxH, (-dis, i))
            if len(maxH) > k:
                heapq.heappop(maxH)
        return [points[idx] for dis, idx in maxH]