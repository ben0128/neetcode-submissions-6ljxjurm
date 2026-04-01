class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        print(heap)
        num = 0
        while num != k-1:
            num += 1
            heapq.heappop(heap)
        return -heap[0]

            