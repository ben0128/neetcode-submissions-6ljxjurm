class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        leftMax, rightMax = height[0], height[n-1]
        vol = 0
        while left <= right:
            if leftMax <= rightMax:
                if leftMax - height[left] > 0:
                    vol += (leftMax - height[left])
                left += 1
                if (left < n):
                    leftMax = max(leftMax, height[left])
            else:
                if rightMax - height[right] > 0:
                    vol += (rightMax - height[right])
                right -= 1
                if (right >= 0):
                    rightMax = max(rightMax, height[right])

        return vol
                


    