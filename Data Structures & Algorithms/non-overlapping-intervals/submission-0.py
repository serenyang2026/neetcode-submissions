class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        num = len(intervals)
        intervals.sort(key = lambda x: x[0])
        preEnd = intervals[0][1]
        non_overlap = 1

        for i in range(1, num):
            if intervals[i][0] >= preEnd:
                non_overlap += 1
                preEnd = intervals[i][1]
            else:
                preEnd = min(preEnd, intervals[i][1])
        
        return num - non_overlap


        