class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # loop through list, add num to list as they are found
        # if num is already in list, return true
        # found_nums = []
        # for n in nums:
        #     if n not in found_nums:
        #         found_nums.append(n)
        #     else:
        #         return True

        # use hash map
        found_nums = {}
        for n in nums:
            found_nums[n] = 0
        
        for n in nums:
            found_nums[n] += 1

        for k in found_nums:
            if found_nums[k] > 1:
                return True

        return False


        