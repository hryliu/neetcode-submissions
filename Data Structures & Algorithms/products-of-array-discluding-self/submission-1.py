class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1) aside from output array

        # get products from left and right
        # prefix_products: [1, 1, 2, 8]
        # suffix_products: [1, 6, 24, 48]

        prefix_products = [0] * (len(nums))
        # suffix_products = [0] * (len(nums))

        prefix_products[0] = 1
        # suffix_products[0] = 1
        
        for i, n in enumerate(nums):
            if i == 0: continue

            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]
            # suffix_products[i] = suffix_products[i - 1] * nums[len(nums) - i]

        # index 0 (48): pp[0] * sp[3]
        # index 1 (24): pp[1] * sp[2]
        # index 2 (12): pp[2] * sp[1]
        # index 3 (8): pp[3] * sp[0]
        output = [0] * len(nums)
        suffix = 1
        for i, n in enumerate(nums):
            print(suffix)
            # output[i] = prefix_products[i] * suffix_products[len(nums) - 1 - i]
            output[len(nums) - 1 - i] = prefix_products[len(nums) - 1 - i] * suffix
            suffix = suffix * nums[len(nums) - 1 - i]

        return output