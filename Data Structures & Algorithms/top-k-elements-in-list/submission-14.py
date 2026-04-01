class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter {[number]: [freq]}
        
        count = Counter(nums)

        # foreach counter to get top k
        min_heap = []
        for num in count:
            heapq.heappush(min_heap, [count[num], num])
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for freq, num in min_heap]