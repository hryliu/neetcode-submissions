class Solution:
    def isPossible(self, piles: List[int], h: int, k: int) -> bool:
        print("k: ", k)
        time = 0
        for p in piles:
            time += math.ceil(p / k)

            if time > h: 
                print("returning false")
                return False

        print("returning true")
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # longest amount of time to eat pile
        max_time = max(piles)
        print("max_time: ", max_time)

        low, high = 1, max_time

        while low < high:
            mid = low + (high - low) // 2
            print("mid: ", mid)
            # search left half of solution space
            if self.isPossible(piles, h, mid):
                high = mid

            else:
                low = mid + 1
            print("low: ", low)
            print("high: ", high)

        return high
