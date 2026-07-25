class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    _sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if _sum == target:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        r -= 1
                        l += 1

                    if _sum > target:
                        r -= 1

                    if _sum < target:
                        l += 1

            
        return res