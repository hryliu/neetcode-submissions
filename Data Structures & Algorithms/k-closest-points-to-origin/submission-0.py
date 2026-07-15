class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        distance_to_points = defaultdict(list)
        out = []

        for p in points:
            x, y = p
            distance = math.sqrt(x*x + y*y)
            heapq.heappush(heap, (distance, p))
            distance_to_points[distance].append(p)

        for i in range(k):
            element = heapq.heappop(heap)
            out.append(element[1])

        return out

        