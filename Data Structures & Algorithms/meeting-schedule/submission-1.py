"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        prevEnd = None
        for item in intervals:
            if prevEnd and item.start < prevEnd:
                return False
            prevEnd = item.end
        return True
                
