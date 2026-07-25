class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * (max(nums) + 1)

        for n in nums:
            buckets[n] += 1

        i = 0
        for j in range(len(buckets)):
            count = buckets[j]
            if count > 0:
                for k in range(i, i + count):
                    nums[k] = j
                i += count

