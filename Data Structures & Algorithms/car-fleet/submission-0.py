class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        prev_time = 0
        fleet = 0

        for p, s in cars:
            time = (target - p) / s

            if time > prev_time:
                prev_time = time
                fleet += 1

        return fleet
