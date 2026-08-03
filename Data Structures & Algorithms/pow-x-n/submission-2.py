class Solution:
    def myPow(self, x: float, n: int) -> float:
        a = 1

        if n < 0:
            c = 1/x
            for i in range(-n):
                a = a*c
        for i in range(n):
            a = a*x
        return a
