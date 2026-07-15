class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        max_len = 1
        curr_len = 1
        sorted_nums = sorted(list(set(nums)))

        print(sorted_nums)

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i + 1] == sorted_nums[i] + 1:
                curr_len += 1
                if curr_len > max_len: 
                    max_len = curr_len
            else:
                curr_len = 1

            print('\n')
            print(sorted_nums[i])
            print("curr len: ", curr_len)
            print("max len:", max_len)

        return max_len
            