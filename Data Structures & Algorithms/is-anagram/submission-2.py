class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Space: O(1) because string was edited in place
        # Time: O(nlogn) 
        if len(s) != len(t):
            return False

        # O(nlogn) for timsort
        s = sorted(s)
        t = sorted(t)

        # O(n)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False

        return True

