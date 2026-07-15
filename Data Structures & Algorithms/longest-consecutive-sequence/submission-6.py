class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums: return 0

        # max_len = 1
        # curr_len = 1
        # sorted_nums = sorted(list(set(nums)))

        # for i in range(len(sorted_nums) - 1):
        #     if sorted_nums[i + 1] == sorted_nums[i] + 1:
        #         curr_len += 1
        #         if curr_len > max_len: 
        #             max_len = curr_len
        #     else:
        #         curr_len = 1

        # return max_len
        if not nums: return 0

        nums_set = set(nums)

        max_length = 1
        for n in nums:
            if n - 1 not in nums_set:
                curr = n
                length = 1
                while (curr + 1 in nums_set):
                    curr += 1
                    length += 1

                max_length = max(length, max_length)

        return max_length

            