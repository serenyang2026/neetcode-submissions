"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        res = 1
        early_end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < early_end:
                res += 1
                early_end = min(early_end, intervals[i].end)
            else:
                early_end = intervals[i].end
        return res
            

        