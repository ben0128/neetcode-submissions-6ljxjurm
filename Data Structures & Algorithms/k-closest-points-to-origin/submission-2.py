class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            distance = math.sqrt((x*x) + (y*y))
            heapq.heappush(max_heap, (-distance, x, y))
        print(max_heap)
        while len(max_heap) > k:
            res = heapq.heappop(max_heap)
            print(res)
        return [[item[1], item[2]] for item in max_heap]
