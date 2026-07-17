class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        # How many of each character t needs.
        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1

        required = len(t_count)   # number of DISTINCT chars in t that must be satisfied
        window_count = defaultdict(int)
        formed = 0                # number of distinct chars currently satisfied in the window

        l = 0
        min_len = float('inf')
        min_start = 0

        for r in range(len(s)):
            char = s[r]
            window_count[char] += 1

            # This char just reached the exact count t needs -> one more requirement satisfied
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # Window is valid (contains all of t) -> try to shrink from the left
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_start = l

                left_char = s[l]
                window_count[left_char] -= 1
                # Removing this char just dropped it below what's needed -> lost a requirement
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1

                l += 1

        return "" if min_len == float('inf') else s[min_start:min_start + min_len]
            

            

        
