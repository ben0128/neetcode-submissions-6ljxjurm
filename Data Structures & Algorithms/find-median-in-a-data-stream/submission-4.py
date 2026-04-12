class MedianFinder:

    def __init__(self):
        self.large = [] # minH
        self.small = [] # maxH

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)
        
        m, n = len(self.large), len(self.small)
        if m - n > 1:
            popEl = heapq.heappop(self.large)
            heapq.heappush(self.small, -popEl)
        if self.large and self.small and self.large[0] < -self.small[0]:
            popEl1 = heapq.heappop(self.large)
            popEl2 = -heapq.heappop(self.small)
            heapq.heappush(self.large, popEl2)
            heapq.heappush(self.small, -popEl1)
    def findMedian(self) -> float:
        m, n = len(self.large), len(self.small)
        if m > n:
            return self.large[0]
        else:
            return (self.large[0]-self.small[0]) / 2