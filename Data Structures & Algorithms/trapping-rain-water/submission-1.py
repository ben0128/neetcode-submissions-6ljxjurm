class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[-1]
        leftArr = []
        rightArr = []
        n = len(height)
        for idx in range(n):
            leftArr.append(leftMax)
            if height[idx] > leftMax:
                leftMax = height[idx]
            rightArr.append(rightMax)
            if height[n-1-idx] > rightMax:
                rightMax = height[n-1-idx]

        print(leftArr, rightArr)
        minArr = []
        # 找出特定位置 左右兩邊的最高點和最低點, 再找出邊界最小值,就能知道該位置能困住多少水
        maxVol = 0
        for idx in range(n):
            diff = min(leftArr[idx], rightArr[n-1-idx]) - height[idx]
            if diff > 0:
                maxVol += diff
        return maxVol