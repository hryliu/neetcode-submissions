class Solution:
    def mySqrt(self, x: int) -> int:
        prev = 0

        for i in range(1, x + 1):
            if i * i > x:
                return prev
            prev = i

        return prev