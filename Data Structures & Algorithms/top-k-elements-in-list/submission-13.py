class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        minH = []

        for n, times in freq.items():
            if len(minH) < k:
                heapq.heappush(minH, (times, n))
            else:
                heapq.heappushpop(minH, (times, n))
        return [n for t, n in minH]


        
        

        






        