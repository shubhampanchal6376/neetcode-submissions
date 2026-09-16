import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        a = []
        n = len(profits)
        for i in range(n):
            t = []
            t.append(capital[i])
            t.append(profits[i])
            a.append(t)
        a.sort()
        idx = 0 
        heap = []
        while k>0:
            while idx < n :
                if a[idx][0] > w:
                    break
                heapq.heappush(heap,-a[idx][1])
                idx+=1
            if len(heap)==0:
                return w
            w = w - heap[0]
            heapq.heappop(heap)
            k-=1
        return w 