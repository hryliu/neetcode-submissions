class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        for word in strs:
            min_len = min(min_len, len(word))

        i = 0
        while i < min_len:
            char = strs[0][i]

            for word in strs[1:]:
                if word[i] != char:
                    return word[:i]
                
            i += 1

        return strs[0][:i]