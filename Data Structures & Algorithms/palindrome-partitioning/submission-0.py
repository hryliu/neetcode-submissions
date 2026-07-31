class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # brute force:
        # generate all substrings
        # check if palindrome 
        # if palindrome, add to set of palindromes

        # time
        # n = len(s)
        # o(2^n) for backtracking
        # o(n^2) for checking all possible substr if they are palindrome
        # space o(n) for recursion stack
        # abcd -> a b c d 
        # ab bc cd
        # abc bcd


        # for every palindrome, we can either add next char or not
        #               []
        #           a           
        #       a       aa
        #           aa      aab
        # aab. aa b

        def isPalindrome(s) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        res = []

        # start = 0
        # end = 1
        # a -> backtrack a
        #   start = 1
        #   a, a -> backtrack b
        #       start = 2

        def backtrack(path, start):
            nonlocal res
            if start == len(s):
                res.append(path[:])
                return

            for i in range(start + 1, len(s) + 1):
                if isPalindrome(s[start : i]):
                    path.append(s[start : i])
                    backtrack(path, i)
                    path.pop()

        backtrack([], 0)
        return res








