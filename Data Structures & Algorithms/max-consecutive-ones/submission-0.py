class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums: return 

        count = 1 if nums[0] == 1 else 0
        res = count

        for i in range(1, len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                res = max(res, count)

        return res
                
        