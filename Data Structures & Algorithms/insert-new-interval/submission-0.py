class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]
        result = []
        for i in range(0, len(intervals)):
            if new_end < intervals[i][0]:
                result.append([new_start, new_end])
                return result + intervals[i:]
            elif new_start > intervals[i][1]:
                result.append(intervals[i])
            else:
                new_start = min(new_start, intervals[i][0])
                new_end = max(new_end, intervals[i][1])
        result.append([new_start, new_end])
        
        return result