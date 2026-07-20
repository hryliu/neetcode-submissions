class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_total = float('-inf')
        total = float('-inf')
       
        for i in range(len(nums)):
            if total < 0 and nums[i] > total:
                total = nums[i]

            else:
                total += nums[i]

            max_total = max(max_total, total)

        return max_total
        