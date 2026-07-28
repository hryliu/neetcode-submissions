class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def helper(n):
            nonlocal seen
            if n == 1:
                return True

            res = 0
            while n > 0:
                res += (n % 10) * (n % 10)
                n = n // 10

            if res in seen:
                return False
            
            seen.add(res)
            return helper(res)

        return helper(n)

        