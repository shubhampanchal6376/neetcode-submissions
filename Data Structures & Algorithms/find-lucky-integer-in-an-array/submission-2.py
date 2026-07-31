class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = {}
        s = []
        for i in arr:
            if i not in m:
                m[i] = 1
            else:
                m[i]+=1
        for i,v in m.items():
            if i==v:
                s.append(i)
        if len(s)==0:
            return -1
        return max(s)