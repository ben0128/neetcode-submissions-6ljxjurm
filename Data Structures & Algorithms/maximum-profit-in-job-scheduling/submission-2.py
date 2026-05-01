from bisect import bisect_right
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        endTimes = [job[0] for job in jobs]
        n = len(startTime)
        # dp[i] , i = job index + 1
        dp = [0] * (n+1)

        # i = job index
        for i, [e, s, p] in enumerate(jobs):
            dpIdx = i+1
            prevDpIdx = bisect_right(endTimes, s)
            tmpMaxProfit = dp[prevDpIdx]+p
            dp[dpIdx] = max(tmpMaxProfit, dp[dpIdx-1])

        return dp[-1]
