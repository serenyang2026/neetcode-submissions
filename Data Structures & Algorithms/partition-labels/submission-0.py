class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, n in enumerate(s):
            lastIndex[n] = i
        
        size, end = 0, 0
        res = []
        for i, n in enumerate(s):
            size += 1
            end = max(end, lastIndex[n])

            if i == end:
                res.append(size)
                size = 0
        return res
        