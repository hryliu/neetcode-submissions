class MedianFinder:
    ## -1 -2
    ## 3 4

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        # move element from min heap to max heap
        if len(self.small) > len(self.large):
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        elif len(self.large) > len(self.small):
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
        
        