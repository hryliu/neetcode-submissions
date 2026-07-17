class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        result = []

        def backtrack(start, combinations, total):
            if total == target:
                result.append(combinations[:])
                return
            elif total > target:
                return

            for i in range(start, len(sorted_candidates)):
                if i > start and sorted_candidates[i] == sorted_candidates[i - 1]:
                    continue
                    
                combinations.append(sorted_candidates[i])
                total += sorted_candidates[i]
                backtrack(i + 1, combinations, total)
                total -= sorted_candidates[i]
                combinations.pop()

        backtrack(0, [], 0)
        return result