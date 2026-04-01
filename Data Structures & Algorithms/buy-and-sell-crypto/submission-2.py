class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        ans = 0
        for price in prices[1:]: 
            if price > minPrice:
                ans = max(price - minPrice, ans)
            else:
                minPrice = price
        return ans