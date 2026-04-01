class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf") for _ in range(n + 1)]
        dp[0], dp[1] = 0, 1
        m = 1
        squreList = []
        for i in range(2, n + 1):
            if m * m <= i:
                squreList.append(m * m)
                m += 1

            for squre in squreList:
                dp[i] = min(dp[i - squre] + 1, dp[i])
        return dp[-1]