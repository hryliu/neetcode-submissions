class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty prefix: exactly one way (do nothing)
        dp[1] = 1  # s[0] != '0' is already guaranteed by the check above

        for i in range(2, n + 1):
            # Single-digit decode: just the current character, s[i-1].
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Two-digit decode: the pair s[i-2:i].
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

            # If NEITHER branch added anything (e.g. s[i-1] == '0' and
            # the two-digit value is out of range), dp[i] correctly
            # stays 0 — there's no way to decode up to this point.

        return dp[n]