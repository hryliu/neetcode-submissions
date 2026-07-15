class Solution:
    def isValid(self, s: str) -> bool:
        # Time: O(n) — single pass through the string.
        # Space: O(n) — stack can hold up to n/2 openings in worst case.
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pairs.values():          # opening
                stack.append(ch)
            else:                              # closing
                if not stack or stack[-1] != pairs.get(ch):
                    return False
                stack.pop()

        return len(stack) == 0