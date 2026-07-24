class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 - 1 2 4 6 - 1
        # prefix
        # 1 1 2 8
        # suffix
        # 1 6 24 48

        prefix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            suffix[i] = suffix[i - 1] * nums[len(nums) - i]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[len(nums) - i - 1])

        return res