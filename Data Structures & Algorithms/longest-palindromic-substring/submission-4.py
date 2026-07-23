class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        max_len = 0

        for i, c in enumerate(s):
            # odd-length palindrome centered on s[i] (e.g. "aba")
            j = 1
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                j += 1  # keep expanding outward while both sides match
            max_len = max(max_len, (j - 1) * 2 + 1)  # j overshot by 1, so real radius is j-1
            if max_len == (j - 1) * 2 + 1:
                res = s[i - j + 1 : i + j]  # slice out the matched palindrome

            # even-length palindrome centered between s[i] and s[i+1] (e.g. "bb")
            j = 0
            while i - j >= 0 and i + j + 1 < len(s) and s[i - j] == s[i + j + 1]:
                j += 1
            max_len = max(max_len, j * 2)
            if max_len == j * 2:
                res = s[i - j + 1 : i + j + 1]

        return res

