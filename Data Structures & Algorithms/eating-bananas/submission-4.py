class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0 
        r = max(piles)
        if sum(piles) <= h:
            return 1
        ans = 0
        while l<=r:
            m = (r+l)//2
            t = 0 
            if m == 0 :
                m+=1
            for i in piles:
                if i % m == 0:
                    t+=i//m
                else:
                    t+=(i//m)+1
            if t <= h:
                ans = m
                r = m -1
            else:
                l = m + 1
        return ans