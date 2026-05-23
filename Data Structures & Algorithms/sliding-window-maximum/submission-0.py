class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        monoQueue = deque([])
        n = len(nums)
        # init mono queue
        for i in range(k-1):
            while monoQueue and nums[monoQueue[-1]] < nums[i]:
                monoQueue.pop()
            monoQueue.append(i)
        ans = [0] * (n-k+1)
        # start loop
        for i in range(k-1, n):
            left = i-k+1
            if monoQueue and monoQueue[0] < left:
                monoQueue.popleft()
            while monoQueue and nums[monoQueue[-1]] < nums[i]:
                monoQueue.pop()
            monoQueue.append(i)
            ans[left] = nums[monoQueue[0]]
        return ans