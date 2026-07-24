class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for i in range(len(nums)):
            count[nums[i]] += 1

        i = 0
        for k, _ in count.items():
            nums[i] = k
            i += 1

        return i