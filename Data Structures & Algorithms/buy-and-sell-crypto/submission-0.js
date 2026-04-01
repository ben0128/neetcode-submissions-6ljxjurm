class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let profit = 0, base = prices[0];
        for (let i=1, len=prices.length;i<len;i++) {
            if (prices[i]<base) base = prices[i];
            else profit = Math.max(profit, prices[i]-base)
        }
        return profit
    }
}
