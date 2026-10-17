import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def hours(s):
            res = 0
            for p in piles:
                res += math.ceil(p/s)
            return res

        res = r
        while l <= r:
            mid = (l + r)//2
            if hours(mid) <= h:
                res = mid
                r = mid - 1
            elif hours(mid) > h:
                l = mid + 1
        
        return res
