class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # count += 1
            l, r = i, i 
            while(l >= 0 and r < len(s) and s[r] == s[l]):
                count += 1
                r += 1
                l -= 1

            l, r = i, i + 1
            while(l >= 0 and r < len(s) and s[r] == s[l]):
                count += 1
                r += 1
                l -= 1

        return count
        