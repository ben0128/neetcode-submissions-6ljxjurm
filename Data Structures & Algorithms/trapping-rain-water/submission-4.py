class Solution:
    def trap(self, height: List[int]) -> int:
        # step 1: preflix sum 
        maxiumLeftSide = [height[0]] # [0, 2, 2, 3, 3, 3, 3, 3, 3, 3]
        maxiumRightSide = [height[-1]] # [1, 2, 3, 3, 3, 3, 3, 3, 3, 3]
        n = len(height)
        res = 0
        for i in range(1, n):
            maxiumLeftSide.append(max(height[i], maxiumLeftSide[-1]))
            maxiumRightSide.append(max(height[n-i-1], maxiumRightSide[-1]))
        # foreach height:
        for i in range(n):
            res += min(maxiumLeftSide[i], maxiumRightSide[n-i-1])-height[i]
        return res