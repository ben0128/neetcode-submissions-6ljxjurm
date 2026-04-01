class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        maxHeight = max(heights)
        maxVol = 0
        while left < right:
            if heights[left] <= heights[right]:
                maxVol = max((right-left)*heights[left], maxVol)
                left += 1
            else:
                maxVol = max((right-left)*heights[right], maxVol)
                right -= 1
            if maxHeight*(right-left) <= maxVol:
                break
        return maxVol