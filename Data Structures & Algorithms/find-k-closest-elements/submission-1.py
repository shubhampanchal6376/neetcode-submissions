import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in arr:
            if len(heap)<k:
                heapq.heappush(heap,(-abs(i-x),-i))
            else:
                if abs(i-x)<-heap[0][0]:
                    heapq.heappushpop(heap,(-abs(i-x),-i))
                elif abs(i-x) == -heap[0][0] and i < -heap[0][1]:
                    heapq.heappushpop(-abs(i-x),-i)
        ans = []
        while heap:
            freq , elem = heapq.heappop(heap)
            ans.append(-elem)
        return sorted(ans)
