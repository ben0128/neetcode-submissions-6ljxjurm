class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        monoQueue = deque([])
        n = len(nums)

        ans = [0] * (n-k+1)
        # start loop
        for i in range(n):
            left = i-k+1
            if monoQueue and monoQueue[0] < left:
                monoQueue.popleft()
            while monoQueue and nums[monoQueue[-1]] < nums[i]:
                monoQueue.pop()
            monoQueue.append(i)
            if left >= 0:
                ans[left] = nums[monoQueue[0]]
                
        return ans