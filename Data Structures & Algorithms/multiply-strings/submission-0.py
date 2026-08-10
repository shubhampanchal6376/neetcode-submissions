class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = {}
        for i in range(0,10):
            m[str(i)] = i
        a = 0 
        b = 0 
        for i in num1:
            a = a*10 + m[i]
        for i in num2:
            b = b*10 + m[i]
        return str(a*b)