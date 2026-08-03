class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 1
        curr_sum = 0
        window = float('inf')

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                window = min(window, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        return window if window != float('inf') else 0