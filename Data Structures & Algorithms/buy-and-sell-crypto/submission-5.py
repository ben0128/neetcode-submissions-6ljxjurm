class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        preflixMin = prices[0]
        maxProfit = 0
        for idx, price in enumerate(prices[1:]):
            preflixMin = min(preflixMin, price)
            maxProfit = max(maxProfit, price-preflixMin)
        return maxProfit