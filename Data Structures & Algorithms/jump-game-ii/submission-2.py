class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        max_reach = 0
        current_end = 0
        count = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == current_end:
                current_end = max_reach
                count += 1
                
        return count

