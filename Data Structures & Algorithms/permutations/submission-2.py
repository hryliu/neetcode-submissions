class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for n in nums:
                if n not in used:
                    path.append(n)
                    used.add(n)
                    backtrack(path, used)
                    used.remove(n)
                    path.pop()

        backtrack([], set())

        return result
            