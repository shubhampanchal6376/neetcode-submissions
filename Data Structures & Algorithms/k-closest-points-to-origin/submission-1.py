import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in points:
            a = i[0]
            b = i[1]
            d = (a**2+b**2)**0.5
            if len(heap)<k:
                heapq.heappush(heap,(-d,i))
            else:
                if d < -heap[0][0]:
                    heapq.heappushpop(heap,(-d,i))
                # elif d == -heap[0][0] and i < heap[0][1]:
                #     heapq.heappushpop(heap,(-d,-i))
        ans = []
        while heap:
            dis , ele = heapq.heappop(heap)
            ans.append(ele)
        return ans
