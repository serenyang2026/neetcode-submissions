class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path= []
        candidates.sort()

        def backtrack(start):

            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path[:])
                return
                
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1)
                path.pop()
            
        backtrack(0)
        return res
