class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = [prices[0]]
        # [1]
        ans = 0
        for price in prices: 
            if price > stack[-1]:
                ans = max(price - stack[-1], ans)
            else:
                while len(stack)>0 and price <= stack[-1]:
                    stack.pop()
                stack.append(price)
        return ans