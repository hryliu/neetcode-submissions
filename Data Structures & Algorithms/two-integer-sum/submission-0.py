class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through nums and use hashmap to track numbers
        # Time: O(n) 
        # Space: O(n)
        num_indexes = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_indexes:
                return [num_indexes[complement], i]
            num_indexes[n] = i


        
                