class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        weight = 0

        for s in stones:
            heapq.heappush(heap, -s)

        while len(heap) > 1:
            largest = -heapq.heappop(heap)
            second_largest = -heapq.heappop(heap)
            heapq.heappush(heap, -(largest - second_largest))

        return -heapq.heappop(heap)