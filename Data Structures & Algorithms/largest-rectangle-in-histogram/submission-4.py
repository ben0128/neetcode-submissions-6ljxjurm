class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for idx, height in enumerate(heights):
            if not stack or stack[-1][1] < height:
                stack.append((idx, height))
            else:
                popIdx = 0
                while stack and stack[-1][1] >= height:
                    popEl = stack.pop()
                    popIdx = popEl[0]
                    maxArea = max(maxArea, (idx-popIdx)*popEl[1])
                stack.append((popIdx, height))

        while stack:
            popEl = stack.pop()
            maxArea = max(maxArea, popEl[1] * (len(heights)-popEl[0]))
        return maxArea

# [7,1,7,2,2,4]

# [1, 2, 2]