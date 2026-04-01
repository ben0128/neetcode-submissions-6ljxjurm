"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        # min_heap
        days = []

        for item in intervals:
            if days and days[0] <= item.start:
                heapq.heappop(days)
            heapq.heappush(days, item.end)
            
        return len(days)
            