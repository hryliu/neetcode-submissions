class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                if i > start and sorted_nums[i] == sorted_nums[i - 1]:
                    continue
                    
                path.append(sorted_nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result

        