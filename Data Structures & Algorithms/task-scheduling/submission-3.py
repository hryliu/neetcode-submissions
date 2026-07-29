class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # maxheap with freq of each char
        # queue with freq, time ready
        # move from maxheap to queue when processed from maxheap
        # move back to maxheap with time is ready

        # XXYY
        # cycles = 0
        # maxheap -2 -2

        # maxheap -2
        # cycles = 1
        # queue (-1, 3)

        # maxheap 
        # cycles = 2
        # queue (-1, 3) (-1, 4)

        count = [0] * 26

        for t in tasks:
            count[ord(t) - ord('A')] += 1

        maxheap = []
        for c in count:
            if c > 0:
                maxheap.append(-c)

        heapq.heapify(maxheap)

        queue = deque()
        cycles = 0
        while maxheap or queue:
            cycles += 1
            if maxheap:
                freq = 1 + heapq.heappop(maxheap)

                if freq < 0:
                    queue.append([freq, cycles + n])

            while queue and cycles == queue[0][1]:
                freq, _ = queue.popleft()
                heapq.heappush(maxheap, freq)

        return cycles


                
            



