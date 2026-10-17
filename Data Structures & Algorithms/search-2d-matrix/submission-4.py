class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = []
        for i in range(len(matrix)):
            m += matrix[i]
        
        l, r = 0, len(m) - 1

        while l <= r:
            mid = (l+r) // 2
            if m[mid] < target:
                l = mid + 1
            elif m[mid] > target:
                r = mid - 1
            else:
                return True
        return False
