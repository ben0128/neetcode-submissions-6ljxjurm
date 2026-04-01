class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [0]*(amount+1)
        memo[0] = 1
        for coin in coins:
            for n in range(amount+1):
                if n - coin >= 0:
                    memo[n] += memo[n-coin]
        return memo[-1]