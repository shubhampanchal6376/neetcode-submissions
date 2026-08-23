class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return a
        x = 0 
        y = 0 
        pow = 0 
        p = a[::-1]
        q = b[::-1]
        for i in range(len(p)):
            if p[i]=="1":
                x+=2**i
        for i in range(len(q)):
            if q[i]=="1":
                y+=2**i
        z = x+y
        ans = ""
        while z>0:
            if z%2==1:
                ans+="1"
            else:
                ans+="0"
            z//=2
        return ans[::-1]
