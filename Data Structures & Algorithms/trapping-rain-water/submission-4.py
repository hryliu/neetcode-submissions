class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0

        l, r = 0, len(height) - 1
        max_left = height[0]
        max_right = height[-1]
        res = 0

        while l < r:
            if height[l] < height[r]:
                diff = max_left - height[l]
                if diff > 0:
                    res += diff
                max_left = max(max_left, height[l])
                l += 1
            else:
                diff = max_right - height[r]
                if diff > 0:
                    res += diff
                max_right = max(max_right, height[r])
                r -= 1

        return res