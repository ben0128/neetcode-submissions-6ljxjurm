class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        dp = [10001] * 10000
        
        for inter in intervals:
            for i in range(inter[0], inter[1]+1):
                dp[i] = min(dp[i], inter[1]-inter[0]+1)
        res = []
        for query in queries:
            if dp[query] == 10001:
                res.append(-1)
            else:
                res.append(dp[query])
        return res
