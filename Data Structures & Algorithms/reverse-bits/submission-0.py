class Solution:
    def reverseBits(self, n: int) -> int:
        b = ""
        while n>0:
            b = str(n%2) + b
            n//=2
        a = b[::-1]
        n = 32 - len(b)
        for i in range(n):
            a+="0"
        n = 0 
        for i in a:
            n = n*2+int(i)
        return n