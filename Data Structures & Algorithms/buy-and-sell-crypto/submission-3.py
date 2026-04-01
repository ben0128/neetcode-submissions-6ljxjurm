class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            if l >= price:
                l = price
            else:
                maxProfit = max(maxProfit, price-l)

        return maxProfit