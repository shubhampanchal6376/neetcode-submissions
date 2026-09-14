class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}

        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1

        heap = []

        for i in m:
            if len(heap) < k:
                heapq.heappush(heap, (m[i], i))
            else:
                if m[i] > heap[0][0]:
                    heapq.heappushpop(heap, (m[i], i))
                elif m[i] == heap[0][0] and i > heap[0][1]:
                    heapq.heappushpop(heap, (m[i], i))

        ans = []

        while heap:
            f, e = heapq.heappop(heap)
            ans.append(e)

        return ans[::-1]