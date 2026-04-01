class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        if amount == 0:
            return 0
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for money in range(1, amount+1):
            for coin in coins:
                if money - coin >= 0:
                    dp[money] = min(1 + dp[money-coin], dp[money])
                else:
                    break
        print(dp)
        return dp[-1] if dp[-1] != amount+1 else -1