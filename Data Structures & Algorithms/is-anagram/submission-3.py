class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Space: O(n) 
        # # Time: O(nlogn) 
        # if len(s) != len(t):
        #     return False

        # # O(nlogn) for timsort
        # s = sorted(s)
        # t = sorted(t)

        # # O(n)
        # for i in range(len(s)):
        #     if s[i] != t[i]:
        #         return False

        # return True

        # Time: O(n+m)
        # Space: O(1)
        # Different lengths -> can't be anagrams
        if len(s) != len(t):
            return False

        # Fixed-size frequency table => O(1) extra space
        count = [0] * 26
        base = ord('a')

        # O(n + m): increment for s, decrement for t
        for ch in s:
            count[ord(ch) - base] += 1
        for ch in t:
            count[ord(ch) - base] -= 1

        # All zeros means same multiset of chars
        return all(c == 0 for c in count)

