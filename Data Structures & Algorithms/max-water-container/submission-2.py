class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        maxVol = 0
        while left < right:
            if heights[left] <= heights[right]:
                maxVol = max((right-left)*heights[left], maxVol)
                print(maxVol)
                left += 1
            else:
                maxVol = max((right-left)*heights[right], maxVol)
                print(maxVol)
                right -= 1
        return maxVol