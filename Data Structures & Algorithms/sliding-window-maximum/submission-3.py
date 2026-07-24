class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_heap = []

        for i in range(0, k - 1):
            heapq.heappush(max_heap, (-nums[i], i))

        for i in range(k - 1, len(nums)):
            while len(max_heap)!= 0 and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)

            heapq.heappush(max_heap, (-nums[i], i))
            res.append(max(nums[i], -max_heap[0][0]))

        return res

