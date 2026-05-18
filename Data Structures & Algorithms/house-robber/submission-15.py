class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 <= nums <= 100
        # 0 <= nums[i] <= 100
        # dp[i] => 一定要搶index i 的房子
        n = len(nums)
        if n <= 1:
            return nums[0]
        dp = [0]*n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # 4, 4,10,10,17
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        
        return dp[-1]
    # nums = [1] => 1
    # nums = [1, 2] => 2
    # nums = [4, 2, 1] => 5
    # nums = [4, 2, 6, 3, 7] => 17
    # dp   = [4, 4,10,10,17]
    # print(rob([1]) == 1)
    # print(rob([1,2]) == 2)
    # print(rob([4,2,1]) == 5)
    # print(rob([4,2,6,3,7]) == 17)
