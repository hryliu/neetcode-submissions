class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # loop through list, add num to list as they are found
        # if num is already in list, return true
        found_nums = []
        for n in nums:
            if n not in found_nums:
                found_nums.append(n)
            else:
                return True

        return False


        