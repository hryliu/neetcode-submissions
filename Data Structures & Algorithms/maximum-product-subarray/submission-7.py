class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        _max, _min = 1, 1

        for n in nums:
            if n == 0:
                _max = 1
                _min = 1
                continue

            temp_max = _max
            _max = max(_max * n, _min * n, n)
            _min = min(temp_max * n, _min * n, n)
            res = max(res, _max, _min)

        return res