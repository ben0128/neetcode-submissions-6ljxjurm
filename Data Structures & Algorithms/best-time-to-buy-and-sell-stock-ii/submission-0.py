class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        ans = 0
        prices.append(0)
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1] and prices[i-1] > low:
                ans += prices[i-1] - low
                low = prices[i]
            elif prices[i] < low:
                low = prices[i]
        return ans
            