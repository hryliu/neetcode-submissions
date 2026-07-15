class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = defaultdict(list)

        for i in range(len(nums)):
            nums_map[nums[i]].append(i)

        print(nums_map)

        for k, v in nums_map.items():
            if target - k in nums_map:
                if len(v) == 1 and k != (target - k):
                    print("here")
                    return [v[0], nums_map[target - k][0]]
                elif len(v) > 1:
                    print("HERE")
                    return [v[0], v[1]]
