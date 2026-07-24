class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        max_count = 0
        max_int = -1

        for num, freq in count.items():
            if freq > max_count:
                max_count = freq
                max_int = num

        return max_int