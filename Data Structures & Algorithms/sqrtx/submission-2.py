class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0 
        r = x
        i = 0 
        while l <= r:
            mid = l + (r-l)//2
            if mid*mid == x:
                i = mid
                break
            elif mid*mid < x:
                l  = mid + 1
                i = mid
            else:
                r = mid-1
        return i