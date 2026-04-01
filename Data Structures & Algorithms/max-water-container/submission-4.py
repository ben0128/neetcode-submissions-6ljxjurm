class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        tmpMax = 0
        while l < r:
            # step 1 : calculate area
            minH = min(heights[l], heights[r])
            # step 2 : memo
            tmpMax = max(tmpMax, minH*(r-l))
            # step 3 : move pointer
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return tmpMax
