class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0 
        j = 0
        for i in range(len(g)):

            while j<len(s):
                if g[i]<=s[j]:
                    cnt+=1
                    j+=1
                    break
                j+=1
        return cnt
        if cnt > len(s):
            return len(s)
        elif cnt > len(g):
            return len(g)
        else:
            return cnt