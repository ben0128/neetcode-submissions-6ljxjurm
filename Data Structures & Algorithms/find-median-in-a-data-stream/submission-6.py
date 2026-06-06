from heapq import heappush, heappop
class MedianFinder:
    def __init__(self):
        self.sH = [] # maxHeap, num inside it need * -1
        self.bH = [] # minHeap

    def addNum(self, num: int) -> None:
        heappush(self.sH, -num)
        if self.bH and -self.sH[0] > self.bH[0]:
            popS, popB = -heappop(self.sH), heappop(self.bH)
            heappush(self.sH, -popB), heappush(self.bH, popS)
        
        if len(self.sH) - len(self.bH) > 1:
            popS = -heappop(self.sH)
            heappush(self.bH, popS)


    def findMedian(self) -> float:
        isEven = (len(self.sH)+len(self.bH)) % 2 == 0
        if isEven:
            return (-self.sH[0]+self.bH[0]) / 2
        else:
            return -self.sH[0]