class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])
        # print(intervals)
        prev_end = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:
                res += 1
                end = min(end, prev_end)
            prev_end = end

        return res