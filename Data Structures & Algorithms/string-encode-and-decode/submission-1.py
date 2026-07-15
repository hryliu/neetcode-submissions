class Solution:

    def encode(self, strs: List[str]) -> str:
        # return '-'.join(s for s in strs)
        # Time: O(m)  (m = total length of all strings)
        # Space: O(m + n) for the output plus small overhead
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        # return list(s.split('-'))

        # Time: O(m)
        # Space: O(m + n) to store the resulting list of strings
        res, i, n = [], 0, len(s)
        while i < n:
            # parse length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1  # skip '#'
            res.append(s[j:j+length])
            i = j + length
        return res