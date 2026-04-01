class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minH = []
        for num in arr:
            if len(minH) < k:
                heapq.heappush(minH, num)
            elif -(minH[0]-x) > num-x:
                heapq.heappushpop(minH, num)
            else:
                break
        return sorted(minH)
                