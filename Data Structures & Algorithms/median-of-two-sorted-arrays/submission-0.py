class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1

        def insert(n):
            nonlocal nums
            low, high = 0, len(nums) - 1

            while(low <= high):
                mid = low + (high - low) // 2

                if n < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            nums.insert(low, n)

        for n in nums2:
            insert(n)

        length = len(nums)
        if length % 2 == 1:
            return nums[(length - 1) // 2]
        else:
            mid = int((length / 2) - 1)
            return (nums[mid] + nums[mid + 1]) / 2

        return 0

        