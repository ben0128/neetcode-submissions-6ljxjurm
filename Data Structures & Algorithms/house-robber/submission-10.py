class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def loop(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(loop(i+2)+ nums[i], loop(i+1)) 
            return dp[i]

        return loop(0)
