class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, temp_nums):
            if len(path) == len(nums):
                result.append(path[:])
                return
            if len(path) > len(nums):
                return

            for n in temp_nums:
                if n not in path:
                    path.append(n)
                    backtrack(path, temp_nums)
                    path.pop()

        for n in nums:
            temp_nums = nums.copy()
            temp_nums.remove(n)
            print(temp_nums)
            backtrack([n], temp_nums)

        return result
            