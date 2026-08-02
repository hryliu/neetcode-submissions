"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
         intervals.sort(key = lambda i : i.start)
         min_start = float('-inf')

         for i in intervals:
            start = i.start
            end = i.end
            if start < min_start:
                return False
            min_start = max(min_start, end)

         return True