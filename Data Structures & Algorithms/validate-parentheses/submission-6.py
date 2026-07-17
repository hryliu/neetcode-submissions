class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: return False

        stack = deque()
        for char in s:
            if not stack or char in ['[', '{', '(']:
                stack.append(char)
            else:
                temp = stack.pop()
                if temp + char not in ['[]', '{}', '()']:
                    return False
        # if stack:
        #     return False
        return True if not stack else False
