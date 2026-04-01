class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [0]*(amount+1)
        memo[0] = 1
        for coin in coins:
            for n in range(coin, amount+1):
                    memo[n] += memo[n-coin]
        return memo[-1]