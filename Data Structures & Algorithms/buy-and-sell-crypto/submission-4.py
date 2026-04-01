class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        preflixMin = [prices[0]] * n
        maxProfit = 0
        for idx, price in enumerate(prices[1:]):
            preflixMin[idx+1] = min(preflixMin[idx], price)
            maxProfit = max(maxProfit, price-preflixMin[idx+1])
        return maxProfit
            