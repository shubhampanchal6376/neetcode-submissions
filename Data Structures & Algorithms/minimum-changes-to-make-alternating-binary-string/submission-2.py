class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = ""
        while len(t)<n:
            t+="0"
            if len(t) == n:
                break
            t+="1"
        p = ""
        while len(p)<n:
            p+="1"
            if len(p) == n:
                break
            p+="0"
        a = 0 
        b = 0 
        for i in range(len(s)):
            if s[i]!=t[i]:
                a+=1
        for i in range(len(s)):
            if s[i]!=p[i]:
                b+=1
        return min(a,b)