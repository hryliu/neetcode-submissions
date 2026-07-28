class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] in nums[:i] or nums[i] in nums[i + 1:]: 
                return nums[i]

