class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        len_nums = len(nums)
        res = []

        print(sorted_nums)
        
        for i, n in enumerate(sorted_nums):
            if (i > 0 and sorted_nums[i] == sorted_nums[i - 1]): continue

            left = i + 1
            right = len_nums - 1

            while(left < right):
                curr_sum = n + sorted_nums[left] + sorted_nums[right]
                if curr_sum == 0:
                    res.append([n, sorted_nums[left], sorted_nums[right]])

                    while (left < right and sorted_nums[left] == sorted_nums[left + 1]):
                        left += 1

                    while (left < right and sorted_nums[right] == sorted_nums[right - 1]):
                        right -= 1

                    left += 1
                    right -= 1
                
                elif curr_sum < 0:
                    left += 1

                if curr_sum > 0:
                    right -=1

        return res