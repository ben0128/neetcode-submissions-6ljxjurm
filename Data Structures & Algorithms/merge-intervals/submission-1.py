class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        currWindow = [intervals[0][0], intervals[0][1]]
        n = len(intervals)
        for i in range(1, n):
            start, end = intervals[i]
            if start <= currWindow[1]:
                currWindow[1] = max(currWindow[1], end)
            else:
                ans.append(currWindow.copy())
                currWindow = [start, end]
        ans.append(currWindow)
        return ans