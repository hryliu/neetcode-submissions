class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # for each char in s3, do dfs to see if it matches char in s1 or s2, if it does, check next char and increment index fo s1
        if not s1 and not s2 and not s3: return True

        if not s3 or len(s1) + len(s2) != len(s3): return False
        
        # abxzcy abc xyz
        # ab i = 2 j = 0
        # x i = 2 j = 1
        # 
        memo = {}

        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if (i, j) in memo: return memo[(i, j)]

            if i < len(s1) and s3[k] == s1[i]:
                if dfs(i + 1, j, k + 1): 
                    memo[(i, j)] = True
                    return True

            if j < len(s2) and s3[k] == s2[j]:
                if dfs(i, j + 1,  k + 1): 
                    memo[(i, j)] = True
                    return True

            print(i, j, k)
            memo[(i, j)] = False
            return False

        return dfs(0, 0, 0)