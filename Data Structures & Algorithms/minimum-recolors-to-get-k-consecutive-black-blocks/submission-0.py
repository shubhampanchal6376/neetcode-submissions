class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0 
        r = k
        n = len(blocks)
        t = []
        for i in blocks:
            t.append(i)
        ans = n
        while r<=n:
            a = t[l:r].count("W")
            if a < ans:
                ans = a
            r+=1
            l+=1
        return ans