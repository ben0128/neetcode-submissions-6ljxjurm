class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l) // 2
            count = 0
            for p in piles:
                count += (p + m - 1) // m
            if count > h:
                l = m+1
            else:
                r = m
        return l