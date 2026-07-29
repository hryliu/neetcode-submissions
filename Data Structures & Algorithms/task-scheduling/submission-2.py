class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # XXYY  n = 2
        # X Y . X Y
        # (1, X) (1, Y) (3, X) (3, Y)
        # (1, X)    1
        # (1, Y)    2
        # (3, X)    3

        # AAABC n = 3
        # A B C . A . . . A
        # (1, A) (4, A) (7, A) (1, B) (1, C)

        # for every task, track earliest time we can add it in hash map
        # add to priority queue
        # track time by adding curr time to time if time is earlier, wait for time if time is later than curr time

        earliest_start = {}
        for i in range(ord('A'), ord('Z') + 1):
            earliest_start[i] = 1

        pq = []
        for t in tasks:
            heapq.heappush(pq, (earliest_start[ord(t)], t))
            earliest_start[ord(t)] += n + 1

        cycles = 0
        while pq:
            start, t = heapq.heappop(pq)

            if start > cycles:
                cycles = start
            
            else:
                cycles += 1

        return cycles
        



        