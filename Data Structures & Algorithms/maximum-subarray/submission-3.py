class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) == 1: return nums[0]
        max_total = float('-inf')
        total = float('-inf')
        reset = True
       
        for i in range(len(nums)):
            # if reset:
            #     total = nums[i]
            #     max_total = max(max_total, total)
            #     reset = False

            # if num is positive, add to subarray
            if total < 0 and nums[i] > total:
                total = nums[i]

            else:
                total += nums[i]
                # max_total = max(max_total, total)
            
            # if number is negative
            # elif i < len(nums) - 1 and total + nums[i] < nums[i + 1]:
            #     reset = True

            max_total = max(max_total, total)

            print(i, ': ', total)

        return max_total
        