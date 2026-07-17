class Solution:
    def isPossible(self, piles: List[int], h: int, k: int) -> bool:
        time = 0
        for p in piles:
            time += math.ceil(p / k)

            if time > h: 
                return False

        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lowest and longest amount of time to eat pile
        low, high = 1, max(piles)

        while low < high:
            mid = low + (high - low) // 2

            # search left half of solution space
            if self.isPossible(piles, h, mid):
                high = mid

            else:
                low = mid + 1

        return high
