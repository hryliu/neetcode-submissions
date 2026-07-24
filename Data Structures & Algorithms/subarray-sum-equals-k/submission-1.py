class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        res = 0
        total = 0

        for n in nums:
            total += n

            diff = total - k
            if diff in prefix_count:
                res += prefix_count[diff]

            prefix_count[total] += 1

        return res


        

        