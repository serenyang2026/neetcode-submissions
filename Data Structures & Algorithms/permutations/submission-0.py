class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path =[]

        def backtrack(nums):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(nums)
                path.pop()
        backtrack(nums)
        return res

