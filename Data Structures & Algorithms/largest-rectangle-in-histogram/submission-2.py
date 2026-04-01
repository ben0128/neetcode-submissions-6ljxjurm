class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for idx, height in enumerate(heights):
            if len(stack) == 0 or stack[-1][1] < height:
                stack.append((idx, height))
            else:
                popIdx = 0
                while len(stack) > 0 and stack[-1][1] >= height:
                    popEl = stack.pop()
                    popIdx = popEl[0]
                    maxArea = max(maxArea, (idx-popIdx)*popEl[1])
                stack.append((popIdx, height))

        while len(stack) > 0:
            popEl = stack.pop()
            temp = 0
            if len(stack) > 0:
                temp = stack[-1][0]
            maxArea = max(maxArea, popEl[1] * (len(heights)-popEl[0]))
        return maxArea
