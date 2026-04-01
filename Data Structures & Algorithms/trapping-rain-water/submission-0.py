class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        leftArr = []
        for h in height:
            leftArr.append(leftMax)
            if h > leftMax:
                leftMax = h

        rightMax = height[-1]
        rightArr = []
        for h in reversed(height):
            rightArr.append(rightMax)
            if h > rightMax:
                rightMax = h
        print(leftArr, rightArr)
        minArr = []
        
        maxVol = 0
        for idx in range(len(height)):
            diff = min(leftArr[idx], rightArr[len(height)-1-idx]) - height[idx]
            if diff > 0:
                maxVol += diff
        return maxVol