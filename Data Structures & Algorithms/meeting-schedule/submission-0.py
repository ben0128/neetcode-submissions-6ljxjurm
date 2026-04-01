"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedList = sorted(intervals, key=lambda x: x.start)
        for idx, ele in enumerate(sortedList):
            print(ele.start)
            if idx == 0:
                continue
            if ele.start < sortedList[idx-1].end:
                return False
        return True