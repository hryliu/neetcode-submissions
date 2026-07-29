class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        #             [0,2,0,3,1,0,1,3,2,1]
        # prefix max   0 0 2 2 3 3 3 3 3 3
        # suffix max   3 3 3 3 3 3 3 2 1 0

        prefix_max, suffix_max = [0] * len(height), [0] * (len(height))
        prefix_max[1] = height[0]
        suffix_max[-2] = height[-1]

        for i in range(2, len(height)):
            prefix_max[i] = max(height[i - 1], prefix_max[i - 1])

        for i in range(len(height) - 3, -1, -1):
            suffix_max[i] = max(height[i + 1], suffix_max[i + 1])

        # print(prefix_max)
        # print(suffix_max)

        water = 0
        for i in range(1, len(height) - 1):
            if height[i] < prefix_max[i] and height[i] < suffix_max[i]:
                water += min(prefix_max[i], suffix_max[i]) - height[i]

        return water
