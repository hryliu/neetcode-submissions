class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp = {}
        # count = 0
        # inc = True

        # def dfs(i, inc, total):
        #     nonlocal count

        #     if inc:
        #         curr_sum = total + nums[i]
        #     else:
        #         curr_sum = total - nums[i]

        #     if i == len(nums) - 1: 
        #         count += 1 if curr_sum == target else 0
        #         return

        #     dfs(i + 1, inc, curr_sum)
        #     dfs(i + 1, not inc, curr_sum)

        # dfs(0, inc, 0)
        # dfs(0, not inc, 0)
        # return count
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])

        return dfs(0, 0)