class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        maxheap = [[-cnt,char] for char , cnt in freq.items()]
        res = ""
        prev = None
        while prev or maxheap:
            if prev and not maxheap:
                return ""
            cnt , char = heapq.heappop(maxheap)
            res+=char
            cnt+=1
            if prev:
                heapq.heappush(maxheap,prev)
                prev = None
            if cnt!=0:
                prev = [cnt,char]
        return res