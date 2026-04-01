class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = nums[:k]
        heapq.heapify(hp)
        
        for el in nums[k:]:
            if el < hp[0]:
                continue
            heapq.heappushpop(hp, el)
        return hp[0]