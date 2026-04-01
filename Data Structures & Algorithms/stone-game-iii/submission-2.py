class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # n = len(stoneValue)
        # dp = [-float('inf')] * (n+1)  

        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if dp[i] > -float('inf'):
        #         return dp[i]

        #     total, res = 0, -float('inf')
        #     for j in range(i, min(i+3, n)):
        #         total += stoneValue[j]
        #         res = max(res, total - dfs(j+1))
        #     dp[i] = res
        #     return dp[i]

        # dfs(0)
        # if dp[0] > 0:
        #     return 'Alice'
        # elif dp[0] < 0:
        #     return 'Bob'
        # else:
        #     return 'Tie'
        n = len(stoneValue)
        dp = [0] * 3
        for i in range(n-1, -1, -1):
            total, res = 0, -float('inf')
            for j in range(i, min(i+3, n)):
                total += stoneValue[j]
                res = max(res, total-dp[j-i])
            dp = [res, dp[0], dp[1]]
        print(dp)
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
    
