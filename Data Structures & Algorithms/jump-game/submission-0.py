class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        cur_position = 0
        cur_value = 0
        while cur_position < goal and cur_value != 0:
            cur_position += nums[cur_position]
            cur_value = nums[cur_postion]
        return cur_value == goal


        