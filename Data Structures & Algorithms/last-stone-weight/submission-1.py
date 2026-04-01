class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        sts = [-stone for stone in stones]
        heapq.heapify(sts)
        
        while len(sts) > 1:
            s1 = heapq.heappop(sts)
            s2 = heapq.heappop(sts)
            if s1 != s2:
                heapq.heappush(sts, -abs(s1-s2))
        
        return -sts[0] if sts else 0