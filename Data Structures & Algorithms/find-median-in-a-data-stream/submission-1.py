import heapq
class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)

    def findMedian(self) -> float:
        n = len(self.l)
        self.l.sort()
        if n%2==0:
            return (self.l[n//2] + self.l[(n//2)-1])/2
        else:
            return self.l[n//2]
        