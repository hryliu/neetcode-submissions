class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        if x_str[0] == '-': return False

        for i in range(len(x_str) // 2):
            if x_str[i] != x_str[len(x_str) - i - 1]:
                return False

        return True