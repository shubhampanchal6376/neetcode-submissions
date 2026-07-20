class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        rem = 0
        while n>1:
            rem = n%2
            n = n//2
            if rem>0:
                return False
        return True