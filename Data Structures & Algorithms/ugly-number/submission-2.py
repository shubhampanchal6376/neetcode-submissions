class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factors in [2,3,5]:
            while n%factors == 0:
                n/=factors
        return n==1