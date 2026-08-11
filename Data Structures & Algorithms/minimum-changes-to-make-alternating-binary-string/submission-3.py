class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = ""
        while True:
            t+="0"
            if len(t) == n:
                break
            t+="1"
            if len(t) == n:
                break
        p = ""
        while True:
            p+="1"
            if len(p) == n:
                break
            p+="0"
            if len(p) == n:
                break
        a = 0 
        b = 0 
        for i in range(len(s)):
            if s[i]!=t[i]:
                a+=1
        for i in range(len(s)):
            if s[i]!=p[i]:
                b+=1
        return min(a,b)