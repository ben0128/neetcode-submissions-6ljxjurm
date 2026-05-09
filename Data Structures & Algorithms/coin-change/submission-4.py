class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for coin in coins:
            for currAmount in range(coin, amount+1):
                # currAmount = index in dp
                dp[currAmount] = min(dp[currAmount-coin]+1, dp[currAmount])
        
        return dp[-1] if dp[-1] < float('inf') else -1