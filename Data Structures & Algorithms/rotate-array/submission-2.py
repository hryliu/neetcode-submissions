class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0 1 2 3

        # 1 2 3 4       0

        # 4 1 2 3       1   arr[3:] + arr[:3] 
        # 3 4 1 2       2   arr[2:] + arr[:2]
        # 2 3 4 1       3   arr[1:] + arr[:1]

        k = k % len(nums)
        first = nums[len(nums) - k:].copy()
        last = nums[:len(nums) - k].copy()

        print(first)
        print(last)

        i = 0
        while i < len(first):
            nums[i] = first[i]
            i += 1

        while i < len(last) + len(first):
            nums[i] = last[i - len(first)]
            i += 1

    
        