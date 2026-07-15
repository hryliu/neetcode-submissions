from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # # Time: O(m*nlogn)
        # # Space: O(m*n)
        # anagrams = {}
        # for s in strs:
        #     sorted_s = ''.join(sorted(s))
        #     if sorted_s not in anagrams.keys():
        #         anagrams[sorted_s] = [s]
        #     else:
        #         anagrams[sorted_s].append(s)

        # anagrams_list = []
        # for v in anagrams.values():
        #     anagrams_list.append(v)
        
        # return anagrams_list

        # Time: O(m*n)
        # Space: O(m)
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26  # assume lowercase a–z
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())