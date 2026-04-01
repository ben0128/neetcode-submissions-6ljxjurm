class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        if n == 2:
            return 1
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 1
        # [0,1,1,0]
        for num in range(3, n+1):
            dp[num] = dp[num-1] + dp[num-2] + dp[num-3]
        return dp[-1]

        
