class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        if len(piles) == h:
            return r
        l = 1
        
        while l < r:
            mid = l + (r-l) // 2
            currH = sum([((p+mid-1)//mid) for p in piles])
            if currH > h:
                l = mid+1
            else:
                r = mid
        return l