class MedianFinder:

    def __init__(self):
        self.left = [] # maxHeap
        self.right = [] # minHeap 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        r, l = len(self.right), len(self.left)
        if l-r > 1:
            popEl = -heapq.heappop(self.left)
            heapq.heappush(self.right, popEl)
        if self.left and self.right and -self.left[0] > self.right[0]:
            pl, pr = -heapq.heappop(self.left), heapq.heappop(self.right)
            heapq.heappush(self.right, pl), heapq.heappush(self.left, -pr)

    def findMedian(self) -> float:
        r, l = len(self.right), len(self.left)
        if r == l:
            return (self.right[0]-self.left[0])/2
        
        return float(-self.left[0])