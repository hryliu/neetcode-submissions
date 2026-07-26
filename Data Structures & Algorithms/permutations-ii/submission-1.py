class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def backtrack(path, remaining):
            if not remaining:
                res.append(path[:])
                return

            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i - 1]:
                    continue
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i + 1:])
                path.pop()

        backtrack([], nums)
        return res