class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        categories = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            categories[sorted_str].append(s)

        return_val = []
        for v in categories.values():
            return_val.append(v)

        return return_val


        