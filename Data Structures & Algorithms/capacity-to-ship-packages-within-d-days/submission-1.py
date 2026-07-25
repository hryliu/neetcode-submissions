class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weight = max(weights)
        max_weight = sum(weights)

        print(min_weight)
        print(max_weight)

        def isValid(limit) -> bool:
            curr = 0
            curr_day = 0

            for w in weights:
                curr += w

                if curr > limit:
                    curr = w
                    curr_day += 1

                if curr == limit:
                    curr = 0
                    curr_day += 1

            if curr != 0: curr_day += 1

            if curr_day > days:
                return False

            return True

        res = max_weight
        while min_weight < max_weight:
            mid = min_weight + (max_weight - min_weight) // 2

            if isValid(mid):
                res = mid
                max_weight = mid

            else:
                min_weight = mid + 1

        return res