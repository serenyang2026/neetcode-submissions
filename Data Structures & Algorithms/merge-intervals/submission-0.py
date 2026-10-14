class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = []
        start, end = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        result.append([start, end])
        return result




