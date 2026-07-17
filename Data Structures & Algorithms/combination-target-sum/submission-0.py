class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, combination, total):
            if total == target:
                result.append(combination[:])
                return
            
            elif total > target:
                return

            for i in range(start, len(nums)):
                combination.append(nums[i])
                total += nums[i]
                backtrack(i, combination, total)
                total -= nums[i]
                combination.pop()

        backtrack(0, [], 0)
        return result