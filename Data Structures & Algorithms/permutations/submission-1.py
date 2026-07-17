class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for n in nums:
                if n not in path:
                    path.append(n)
                    backtrack(path)
                    path.pop()

        
        backtrack([])

        return result
            