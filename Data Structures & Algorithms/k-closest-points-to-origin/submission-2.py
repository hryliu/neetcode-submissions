class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        out = []

        for x, y in points:
            distance = -(x*x + y*y)

            if len(heap) < k: 
                heapq.heappush(heap, (distance, (x, y)))

            else:
                if distance > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (distance, (x, y)))

        return [p for (_, p) in heap]

        