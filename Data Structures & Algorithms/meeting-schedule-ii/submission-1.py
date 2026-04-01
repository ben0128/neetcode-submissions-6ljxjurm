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
        days = []

        for idx in range(0, len(intervals)):
            item = intervals[idx]
            isAdd = False
            for day in days:
                if day[-1].end <= item.start:
                    day.append(item)
                    isAdd = True
                    break
            if not isAdd:
                days.append([item])
        print(days)
        return len(days)
            