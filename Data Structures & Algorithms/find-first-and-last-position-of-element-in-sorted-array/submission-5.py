class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        first, last = -1, -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1

            # search right half
            elif nums[mid] < target:
                low = mid + 1

            # search left half
            else:
                high = mid - 1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1

            # search right half
            elif nums[mid] < target:
                low = mid + 1

            # search left half
            else:
                high = mid - 1

        return [first, last]